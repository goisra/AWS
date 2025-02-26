# Proyecto de Gestión de Identidades y Accesos en AWS

Este proyecto está diseñado para crear una infraestructura segura de gestión de identidades y accesos en AWS, implementando mejores prácticas de seguridad, autenticación multifactor (MFA), federación con Active Directory, auditoría de accesos y optimización de roles y permisos.

## Objetivos Claves

✅ **Gestión de usuarios y accesos**: Implementar **IAM** y **AWS Identity Center** para administrar permisos y accesos centralizados.  
✅ **Seguridad con MFA**: Configurar **autenticación multifactor** (MFA) para proteger cuentas de usuarios en AWS.  
✅ **Federación con Active Directory**: Integrar **AWS** con **Active Directory** (AD) para gestionar identidades empresariales.  
✅ **Monitoreo y auditoría**: Usar **AWS CloudTrail**, **AWS Config** y **AWS Security Hub** para registrar accesos y detectar anomalías.  
✅ **Optimización de permisos**: Implementar el **principio de menor privilegio** con **políticas IAM** y **Access Analyzer**.

## Arquitectura del Proyecto

### 📌 1. **AWS IAM (Identity and Access Management)**

- **Creación de usuarios, roles y políticas IAM** con permisos mínimos, asegurando que los usuarios solo tengan los permisos necesarios para realizar su trabajo.
- **Configuración de grupos IAM** con permisos según el rol del usuario para facilitar la gestión y administración de permisos.

### 📌 2. **AWS Identity Center (SSO)**

- **Implementación de acceso centralizado** mediante **AWS Identity Center**, permitiendo un inicio de sesión único (SSO) para los usuarios.
- **Integración con Active Directory (AD)** para la federación de usuarios, facilitando la gestión de identidades empresariales.
- **Configuración de MFA obligatorio** en **AWS Identity Center** para mejorar la seguridad de las cuentas de los usuarios.

### 📌 3. **Seguridad y Auditoría**

- **Activación de AWS CloudTrail** para monitorear accesos y cambios en los permisos de usuarios, ayudando a detectar acciones sospechosas.
- **Uso de AWS Config** para detectar configuraciones inseguras (ej. usuarios sin MFA) y garantizar que las configuraciones estén alineadas con las mejores prácticas de seguridad.
- **Implementación de AWS Security Hub** para consolidar y centralizar las alertas de seguridad, mejorando la visibilidad sobre la postura de seguridad.

### 📌 4. **Optimización y Evaluación de Seguridad**

- **Uso de IAM Access Analyzer** para identificar permisos excesivos y asegurarse de que los usuarios solo tengan acceso a los recursos que realmente necesitan.
- **Aplicación del AWS Well-Architected Framework** (Security Pillar) para mejorar la seguridad de la infraestructura, asegurando que se sigan las mejores prácticas en cuanto a accesos y control.

## Beneficios Claves

- **Seguridad Mejorada**: Implementación de MFA y acceso controlado a través de IAM y AWS Identity Center.
- **Cumplimiento y Auditoría**: Registro detallado de acciones y cambios en los recursos de AWS, facilitando la auditoría de accesos.
- **Gestión Centralizada**: Integración con Active Directory para la federación de identidades, simplificando la administración de usuarios y accesos.
- **Optimización Continua**: Uso de herramientas como IAM Access Analyzer y AWS Security Hub para mejorar y asegurar la infraestructura de forma continua.

## Requisitos

- Cuenta de AWS con permisos de administrador.
- Active Directory (o configuración para federación de identidades).
- Conocimientos básicos en IAM, AWS Identity Center, y servicios de seguridad en AWS.

## Documentación Adicional

Si necesitas más información sobre cómo configurar estos servicios, consulta la siguiente documentación oficial de AWS:

- [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/)
- [AWS Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/)
- [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/)
- [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/)
- [AWS Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/)
- [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer.html)

