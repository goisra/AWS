
# Sistema de Monitoreo de Estacionamiento Inteligente con AWS SNS

Este proyecto es un **sistema de monitoreo para estacionamientos inteligentes** que utiliza sensores para detectar la entrada y salida de vehículos en un estacionamiento. La solución incluye la integración con **AWS SNS (Simple Notification Service)** para enviar alertas automáticas sobre eventos importantes como bloqueos de sensores o mantenimiento preventivo de las barreras de entrada y salida.

### Características principales:

- **Detección de vehículos** en tiempo real utilizando sensores ultrasónicos conectados a un microcontrolador.
- **Interfaz gráfica de usuario (GUI)** construida con Tkinter, mostrando estadísticas del estacionamiento y el estado de las barreras.
- **Alertas automáticas por correo electrónico** o a través de SNS cuando se detectan problemas, como bloqueos o la necesidad de mantenimiento.
- **Mantenimiento preventivo** basado en el número de usos de las barreras de entrada y salida.
- **Registro de eventos** de entrada y salida de vehículos en un archivo CSV para monitoreo.

Este sistema es ideal para estacionamientos automatizados que requieren monitoreo constante y notificaciones sobre el estado del equipo y la ocupación.

---

## Características

- **Monitoreo en tiempo real** de la ocupación del estacionamiento y el estado de las barreras.
- **Alertas automáticas a través de AWS SNS** por correo electrónico en caso de fallos en el sistema.
- **Mantenimiento preventivo** y alertas cuando las barreras alcanzan un número específico de usos.
- **Registro de eventos** para mantener un historial completo de los movimientos de vehículos.
- **Interfaz gráfica** que visualiza el estado de los sensores, las barreras y las estadísticas en tiempo real.

---

## Requisitos

Para ejecutar este proyecto, necesitas tener configurado lo siguiente:

- **Python 3.6 o superior**.
- **Librerías necesarias**:
  - `boto3` (para interactuar con AWS SNS).
  - `pyserial` (para leer datos desde el puerto serial).
  - `tkinter` (para la interfaz gráfica).
  - `smtplib` (para enviar correos electrónicos en caso de alertas).
  - `csv` (para registrar los eventos).

Puedes instalar las librerías necesarias con el siguiente comando:

```bash
pip install boto3 pyserial
```

Además, asegúrate de tener una cuenta de **AWS** configurada con **SNS** habilitado y las credenciales necesarias para interactuar con el servicio. Para obtener más detalles sobre la configuración de SNS en AWS, consulta la [documentación oficial de AWS SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html).

---

## Instalación y Configuración

1. **Configura tu hardware**:
   - Conecta un **sensor ultrasónico** (o similar) a un **Microcontrolador** que se encargue de leer las entradas y salidas de los vehículos.
   - Asegúrate de que el Microcontrolador esté conectado al puerto serial correcto.

2. **Clona o descarga el proyecto**:
   - Puedes clonar el repositorio o descargar el código directamente en tu máquina local.
   
   ```bash
   git clone https://github.com/tu_usuario/sistema_estacionamiento.git
   ```

3. **Configuración del puerto serial**:
   - Asegúrate de que el puerto serial esté configurado correctamente en el código. Si tu dispositivo está conectado a un puerto diferente, actualiza esta línea:
   
   ```python
   arduino = serial.Serial('COM6', 9600, timeout=1)  # Cambia 'COM6' por el puerto correcto
   ```

4. **Configura AWS SNS**:
   - Crea un **SNS Topic** en la consola de AWS y obtén el ARN (Amazon Resource Name) de tu SNS Topic.
   - Actualiza el archivo de código con tu ARN de SNS:

   ```python
   sns_topic_arn = 'arn:aws:sns:us-east-1:123456789012:MySNSTopic'
   ```

5. **Configura el correo electrónico**:
   - Si decides recibir alertas por correo electrónico, asegúrate de tener configurado un correo electrónico SMTP (por ejemplo, Gmail) en el código.

---

## Cómo Probar el Proyecto

1. **Ejecuta el script**:
   Una vez configurado todo, ejecuta el archivo Python principal para iniciar el sistema.

   ```bash
   python sistema_estacionamiento.py
   ```

   Esto abrirá la **interfaz gráfica** donde podrás ver en tiempo real el estado de las barreras y la ocupación del estacionamiento.

2. **Simula la entrada y salida de vehículos**:
   Coloca objetos frente a los sensores ultrasónicos para simular el ingreso y salida de vehículos. La interfaz se actualizará automáticamente para reflejar el cambio en el número de vehículos que han entrado o salido.

3. **Recibe alertas de AWS SNS**:
   Cuando se detecte un problema (como un sensor bloqueado o un mantenimiento requerido), el sistema enviará alertas a través de **AWS SNS** a los suscriptores configurados.

---

## Funcionalidades de AWS SNS

### **Notificaciones Automáticas**

El sistema está integrado con **AWS SNS** para enviar notificaciones de alerta. Cuando se detecte un fallo, como un sensor bloqueado o la necesidad de mantenimiento en las barreras, el sistema envía una notificación a un **Topic de SNS** configurado previamente.

```python
def enviar_mensaje_sns(mensaje):
    try:
        response = sns_client.publish(
            TopicArn=sns_topic_arn,
            Message=mensaje,
            Subject="Alerta de Estacionamiento"
        )
        print(f"Mensaje enviado a SNS: {response['MessageId']}")
    except Exception as e:
        print(f"Error al enviar el mensaje a SNS: {e}")
```

### **Subscripción al Topic SNS**

Puedes suscribir tu correo electrónico o cualquier otro endpoint al Topic SNS para recibir las alertas. Asegúrate de configurar correctamente las **credenciales de AWS** en tu entorno local, utilizando el archivo de configuración de AWS CLI o las variables de entorno.

---

## Registro de Eventos

El sistema mantiene un archivo CSV con un registro de todos los eventos de entrada y salida de vehículos. Este archivo se actualiza automáticamente con la siguiente información:

```csv
Fecha y Hora, Tipo de Evento, Entradas Totales, Salidas Totales
2024-12-10 10:00:00, Entrada, 1, 0
2024-12-10 10:05:00, Salida, 1, 1
```

---

## Contribuciones

Si deseas contribuir a este proyecto, puedes hacer un **fork** del repositorio y enviar un **pull request** con tus mejoras o correcciones. Asegúrate de seguir las mejores prácticas de codificación y documentar cualquier cambio realizado.

---

## Licencia

Este proyecto está licenciado bajo la **MIT License**. Puedes usar, modificar y distribuir este código según los términos de la licencia.

---
