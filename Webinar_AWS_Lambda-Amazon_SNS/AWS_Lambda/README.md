### Crear la función Lambda para procesar pedidos

Crea una función Lambda que se active con los eventos de DynamoDB Streams. Esta función será la encargada de procesar los detalles del pedido y publicarlos en un tema SNS.

**Permisos requeridos**: La función Lambda necesitará permisos para leer desde DynamoDB Streams y publicar mensajes en SNS.