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
            
            #Mensaje para el correo
            message = f"Nuevo pedido:\nCliente: {cliente}\nProducto: {producto}\nCantidad: {cantidad}"
            
            # Enviar el mensaje por SNS
            sns_client.publish(
                TopicArn='Nombre del ARN',  
                Message=message,
                Subject='Nuevo pedido recibido'
            )
    return {'statusCode': 200, 'body': 'Correo enviado correctamente'}
