import serial
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import csv
import smtplib
from email.mime.text import MIMEText
import boto3

# Configuración del puerto serial
try:
    arduino = serial.Serial('COM6', 9600, timeout=1)  # Cambia 'COM6' según tu configuración
except Exception as e:
    print(f"Error al conectar con el Arduino: {e}")
    exit()

# Configuración de AWS SNS
sns_client = boto3.client('sns', region_name='us-east-1')
sns_topic_arn = 'arn:aws:sns:us-east-1:123456789012:MySNSTopic'

# Función para enviar mensajes a SNS
def enviar_alerta(mensaje):
    try:
        response = sns_client.publish(
            TopicArn=sns_topic_arn,
            Message=mensaje,
            Subject="Alerta de Estacionamiento"
        )
        print(f"Mensaje enviado a SNS: {response['MessageId']}")
    except Exception as e:
        print(f"Error al enviar el mensaje a SNS: {e}")

# Variables globales
vehiculos_entraron = 0
vehiculos_salieron = 0
capacidad_total = 50
sensor_entrada_activado = False
sensor_salida_activado = False
contador_entrada_uso = 0
contador_salida_uso = 0
tiempo_sensor_entrada = None
tiempo_sensor_salida = None
estado_servo_entrada = "Cerrado"
estado_servo_salida = "Cerrado"
correo_enviado_entrada = False
correo_enviado_salida = False

# Función para actualizar el estado
def actualizar_estado():
    global vehiculos_entraron, vehiculos_salieron, sensor_entrada_activado, sensor_salida_activado
    global contador_entrada_uso, contador_salida_uso, tiempo_sensor_entrada, tiempo_sensor_salida
    global estado_servo_entrada, estado_servo_salida, correo_enviado_entrada, correo_enviado_salida

    try:
        # Leer datos del puerto serial
        data = arduino.readline().decode('utf-8').strip()
        if data and "," in data:
            distancia_entrada, distancia_salida = map(int, data.split(","))

            # Detectar si el sensor de entrada se activa
            if distancia_entrada <= 15:
                if not sensor_entrada_activado:
                    vehiculos_entraron += 1
                    contador_entrada_uso += 1
                    registrar_evento("Entrada")
                    actualizar_tabla("Entrada")
                    sensor_entrada_activado = True
                    tiempo_sensor_entrada = datetime.now()
                    estado_servo_entrada = "Abierto"
                    actualizar_estado_servo()

            # Detectar si el sensor de salida se activa
            if distancia_salida <= 15:
                if not sensor_salida_activado:
                    if vehiculos_entraron > vehiculos_salieron:
                        vehiculos_salieron += 1
                        contador_salida_uso += 1
                        registrar_evento("Salida")
                        actualizar_tabla("Salida")
                        sensor_salida_activado = True
                        tiempo_sensor_salida = datetime.now()
                        estado_servo_salida = "Abierto"
                        actualizar_estado_servo()
                    else:
                        print("Advertencia: No puede haber más salidas que entradas.")

            # Resetear los sensores cuando el vehículo ya no esté presente
            if distancia_entrada > 15:
                sensor_entrada_activado = False
                estado_servo_entrada = "Cerrado"
                actualizar_estado_servo()

            if distancia_salida > 15:
                sensor_salida_activado = False
                estado_servo_salida = "Cerrado"
                actualizar_estado_servo()

            # Verificar tiempos prolongados de activación del sensor
            ahora = datetime.now()
            if sensor_entrada_activado and tiempo_sensor_entrada and (ahora - tiempo_sensor_entrada).seconds >= 15:
                if not correo_enviado_entrada:
                    enviar_alerta("Advertencia: Sensor de entrada bloqueado o pluma atascada.")
                    correo_enviado_entrada = True

            if sensor_salida_activado and tiempo_sensor_salida and (ahora - tiempo_sensor_salida).seconds >= 15:
                if not correo_enviado_salida:
                    enviar_alerta("Advertencia: Sensor de salida bloqueado o pluma atascada.")
                    correo_enviado_salida = True

            # Mostrar sugerencia de mantenimiento preventivo
            if contador_entrada_uso == 20:
                enviar_alerta("Mantenimiento Preventivo: La barrera de entrada requiere mantenimiento preventivo.")
                contador_entrada_uso = 0

            if contador_salida_uso == 20:
                enviar_alerta("Mantenimiento Preventivo: La barrera de salida requiere mantenimiento preventivo.")
                contador_salida_uso = 0

            # Actualizar indicadores visuales
            actualizar_contadores()
    except Exception as e:
        print(f"Error al procesar datos: {e}")
    
    root.after(150, actualizar_estado)

# Función para registrar eventos
def registrar_evento(tipo):
    with open("registro_estacionamiento.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), tipo])

# Función para actualizar la tabla
def actualizar_tabla(tipo):
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    table.insert("", "end", values=(fecha_hora, tipo, vehiculos_entraron, vehiculos_salieron))

# Función para actualizar el estado de los servos
def actualizar_estado_servo():
    # Cambiar texto y color del Servo Entrada
    if estado_servo_entrada == "Abierto":
        servo_entrada_label.config(text=f"Servo Entrada: {estado_servo_entrada}", bg="green", fg="white")
    else:
        servo_entrada_label.config(text=f"Servo Entrada: {estado_servo_entrada}", bg="red", fg="white")
    
    # Cambiar texto y color del Servo Salida
    if estado_servo_salida == "Abierto":
        servo_salida_label.config(text=f"Servo Salida: {estado_servo_salida}", bg="green", fg="white")
    else:
        servo_salida_label.config(text=f"Servo Salida: {estado_servo_salida}", bg="red", fg="white")

# Función para actualizar los contadores
def actualizar_contadores():
    ocupacion_actual = vehiculos_entraron - vehiculos_salieron
    porcentaje_ocupacion = (ocupacion_actual / capacidad_total) * 100
    ocupacion_label.config(text=f"Ocupación Actual: {ocupacion_actual} / {capacidad_total} ({porcentaje_ocupacion:.2f}%)")

    contador_entrada_label.config(text=f"Entradas: {vehiculos_entraron}")
    contador_salida_label.config(text=f"Salidas: {vehiculos_salieron}")

    # Cambiar color de la ocupación dependiendo del estado
    if ocupacion_actual >= capacidad_total:
        ocupacion_label.config(bg="red", fg="white")
    else:
        ocupacion_label.config(bg="green", fg="white")

# Interfaz gráfica
root = tk.Tk()
root.title("Sistema de Monitoreo de Estacionamiento")
root.geometry("800x600")

# Panel de estadísticas
stats_frame = tk.Frame(root)
stats_frame.pack(pady=10)

contador_entrada_label = tk.Label(stats_frame, text="Entradas: 0", font=("Arial", 16))
contador_entrada_label.grid(row=0, column=0, padx=10)

contador_salida_label = tk.Label(stats_frame, text="Salidas: 0", font=("Arial", 16))
contador_salida_label.grid(row=0, column=1, padx=10)

ocupacion_label = tk.Label(stats_frame, text="Ocupación Actual: 0 / 50", font=("Arial", 16))
ocupacion_label.grid(row=0, column=2, padx=10)

# Panel de servos
servo_frame = tk.Frame(root)
servo_frame.pack(pady=10)

servo_entrada_label = tk.Label(servo_frame, text="Servo Entrada: Cerrado", font=("Arial", 16), bg="red", fg="white")
servo_entrada_label.grid(row=0, column=0, padx=10)

servo_salida_label = tk.Label(servo_frame, text="Servo Salida: Cerrado", font=("Arial", 16), bg="red", fg="white")
servo_salida_label.grid(row=0, column=1, padx=10)

# Tabla de eventos
table_frame = tk.Frame(root)
table_frame.pack(pady=20)

columns = ("Fecha y Hora", "Tipo", "Entradas", "Salidas")
table = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)
table.heading("Fecha y Hora", text="Fecha y Hora")
table.heading("Tipo", text="Tipo")
table.heading("Entradas", text="Entradas")
table.heading("Salidas", text="Salidas")
table.pack()

# Iniciar el monitoreo
actualizar_estado()

# Ejecutar la interfaz gráfica
root.mainloop()
