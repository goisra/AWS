import boto3
import json

sns_client = boto3.client('sns')

def lambda_handler(event, context):
    print("Event received:", json.dumps(event))
    
    for record in event['Records']:
        print("Processing record:", record)
        
        if record['eventName'] == 'INSERT':
            pedido = record['dynamodb']['NewImage']
            cliente = pedido['Cliente']['S']
            producto = pedido['Producto']['S']
            cantidad = pedido['Cantidad']['N']
            
            message = f"Nuevo pedido:\nCliente: {cliente}\nProducto: {producto}\nCantidad: {cantidad}"
            
            try:
                response = sns_client.publish(
                    TopicArn='arn:aws:sns:us-east-1:992382420467:Pedidos',  # Reemplaza con tu ARN real
                    Message=message,
                    Subject='Nuevo pedido recibido'
                )
                print("SNS response:", response)
            except Exception as e:
                print("Error sending SNS:", str(e))
    
    return {'statusCode': 200, 'body': 'Procesado correctamente'}
