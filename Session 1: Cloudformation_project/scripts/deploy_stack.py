import boto3
import sys

# Parámetros del stack
STACK_NAME = "my-sns-stack"
TEMPLATE_FILE = "../templates/sns_topic_cloudformation.yaml"

def deploy_stack():
    # Cargar el archivo de plantilla
    try:
        with open(TEMPLATE_FILE, 'r') as template_file:
            template_body = template_file.read()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {TEMPLATE_FILE}")
        sys.exit(1)

    # Cliente de CloudFormation
    cf_client = boto3.client('cloudformation')

    # Crear el stack
    try:
        response = cf_client.create_stack(
            StackName=STACK_NAME,
            TemplateBody=template_body,
            Capabilities=['CAPABILITY_NAMED_IAM'],  # Necesario si se usan roles IAM
        )
        print(f"Stack creado con éxito: {response['StackId']}")
    except Exception as e:
        print(f"Error al crear el stack: {e}")

if __name__ == "__main__":
    deploy_stack()
