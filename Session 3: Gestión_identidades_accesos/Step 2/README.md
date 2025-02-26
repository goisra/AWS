# Configuración de IAM Identity Center en AWS con MFA

Este documento describe los pasos para acceder, configurar y habilitar MFA (Autenticación Multifactor) en IAM Identity Center de AWS, además de cómo agregar usuarios y asignarles accesos.

## Pasos para configurar IAM Identity Center y habilitar MFA

### 1. Acceder al IAM Identity Center
- Inicia sesión en la [Consola de AWS](https://aws.amazon.com/console/).
- En la barra de búsqueda, escribe **IAM Identity Center**.
- Haz clic en **IAM Identity Center**.

### 2. Configurar IAM Identity Center
Si es la primera vez que accedes al IAM Identity Center, necesitarás habilitarlo.

#### Habilitar IAM Identity Center:
- Si aún no lo has habilitado, se te pedirá que lo configures.
- Haz clic en el botón **Habilitar** para activar IAM Identity Center.

#### Configurar fuente de identidad:
- Te ofrecerán dos opciones:
  1. **Usar IAM Identity Center** como fuente de identidad interna: Esto te permitirá gestionar los usuarios directamente dentro de AWS.
  2. **Integrar con Active Directory** o alguna fuente externa de identidad (por ejemplo, Azure AD o un AD local): Si ya tienes un directorio de identidades, puedes integrarlo.

Si eliges gestionar usuarios directamente en AWS, selecciona la opción de **IAM Identity Center** y continúa.

### 3. Habilitar MFA en IAM Identity Center
- En la página de configuración de IAM Identity Center, busca la sección de **Autenticación multifactor (MFA)**.
- Habilita **MFA** para los usuarios de IAM Identity Center.
- Puedes elegir entre usar un **dispositivo MFA virtual** (como Google Authenticator o Authy) o habilitar **MFA de hardware** si prefieres un dispositivo físico.

### 4. Crear Usuarios en IAM Identity Center
#### Agregar Usuarios:
- En el panel de IAM Identity Center, ve a la sección de **Usuarios** y selecciona **Agregar usuario**.

#### Configurar las credenciales:
- Aquí podrás asignar nombres y credenciales para los usuarios, además de establecer si deben usar una contraseña específica para iniciar sesión.

### 5. Asignar Accesos a los Usuarios
#### Grupos y Roles:
- Asocia a los usuarios a los **grupos de acceso** que hayas creado previamente para definir qué permisos tendrán en las cuentas de AWS.
- Asocia los usuarios a las **cuentas de AWS** que deseas gestionar desde IAM Identity Center.

### 6. Habilitar MFA para cada Usuario
Para hacer **MFA obligatorio** para los usuarios de IAM Identity Center:
- Dentro de la consola de IAM Identity Center, selecciona el usuario al que deseas habilitar MFA.
- Busca la sección de **Seguridad** y selecciona la opción para habilitar MFA.
- Cuando el usuario inicie sesión por primera vez, se le pedirá configurar MFA utilizando una aplicación como Google Authenticator.

### 7. Probar el Acceso del Usuario
- Después de configurar MFA, pide a un usuario que inicie sesión en la consola de IAM Identity Center.
- El usuario deberá ingresar su **nombre de usuario** y **contraseña**.
- Luego, se le pedirá que ingrese el **código MFA** generado por la aplicación de autenticación (como Google Authenticator o Authy).

---

Si necesitas más información sobre cómo gestionar usuarios o configurar IAM Identity Center, consulta la [documentación oficial de AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/).