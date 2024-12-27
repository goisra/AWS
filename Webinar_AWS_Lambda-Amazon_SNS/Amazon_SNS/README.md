### Crear el tema SNS

Crea un tema SNS llamado `Pedidos`. Este tema será utilizado para enviar las notificaciones sobre los pedidos.

### 4. Crear los suscriptores

- **Correo electrónico**: Configura una suscripción de tipo correo electrónico al tema SNS. Ingresa una dirección de correo electrónico donde se enviarán las notificaciones.
- **SQS**: Crea una cola de mensajes en SQS que recibirá los detalles del pedido para el sistema de facturación.
- **Lambda**: Crea una función Lambda adicional que se suscriba al tema SNS y envíe los detalles del pedido al sistema de logística.

### 5. Configuración de la suscripción en SNS

Suscribe la función Lambda, la cola de SQS y la dirección de correo electrónico al tema SNS "Pedidos". Configura los tipos de notificación que deben enviarse a cada suscriptor.