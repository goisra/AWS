# Sistema de Notificación de Procesamiento de Pedidos

Este proyecto muestra cómo implementar un sistema de notificación de procesamiento de pedidos en una tienda en línea utilizando servicios de AWS como **SNS**, **Lambda** y **DynamoDB Streams**. El sistema permite notificar diferentes áreas cuando se realiza un pedido, facilitando la automatización de flujos de trabajo y mejorando la eficiencia en el proceso de ventas.

## Escenario

Una tienda en línea quiere notificar varias partes interesadas cuando se realice un pedido. Estas partes incluyen al cliente (para confirmar el pedido), al sistema de facturación (para procesar el pago) y al sistema de envío/logística (para organizar el envío del producto).

### Componentes del Sistema

1. **Publicador (Lambda)**: Una función AWS Lambda que se activa cuando se cargan nuevos pedidos en una tabla de DynamoDB mediante Streams. Esta función se encarga de procesar el evento y publicar los detalles del pedido en un tema SNS.

2. **Tema SNS ("Pedidos")**: Un tema de Amazon SNS al que la Lambda publica los detalles del pedido. Los suscriptores a este tema reciben las notificaciones.

3. **Suscriptores**:
   - **Correo electrónico**: Notificación enviada al cliente para informarle que su pedido fue recibido.
   - **Lambda**: Un Lambda que maneja la notificación y envío de detalles del pedido al sistema de envíos/logística.

## Flujo del Sistema

1. **Cliente realiza un pedido** en la tienda en línea.
2. **DynamoDB** registra el pedido en la tabla `Pedidos`.
3. Un evento de DynamoDB Stream activa una **función Lambda** que procesa el pedido.
4. La Lambda publica los detalles del pedido en el **tema SNS "Pedidos"**.
5. **SNS** distribuye la notificación a los siguientes suscriptores:
   - Un **correo electrónico** es enviado al cliente confirmando que su pedido ha sido recibido.
   - Un **mensaje** es enviado a **SQS**, que alimenta el sistema de facturación para procesar el pago.
   - Un **evento** es enviado a otro **Lambda**, que coordina con el sistema de envío/logística para organizar el despacho del pedido.
