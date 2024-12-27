import boto3

# Crear el cliente de SNS
sns_client = boto3.client('sns')

# Función Lambda
def lambda_handler(event, context):
    for record in event['Records']:
        # Extraer el nuevo registro de DynamoDB
        if record['eventName'] == 'INSERT':
            pedido = record['dynamodb']['NewImage']
            cliente = pedido['Cliente']['S']
            producto = pedido['Producto']['S']
            cantidad = pedido['Cantidad']['N']
            
            # Crear el mensaje para el correo
            message = f"Nuevo pedido:\nCliente: {cliente}\nProducto: {producto}\nCantidad: {cantidad}"
            
            # Enviar el mensaje por SNS
            sns_client.publish(
                TopicArn='arn:aws:sns:us-east-1:992382420467:Pedidos',  # Asegúrate de que este ARN esté correcto
                Message=message,
                Subject='Nuevo pedido recibido'
            )
    return {'statusCode': 200, 'body': 'Correo enviado correctamente'}