# Configuración de Grupo IAM con Permisos Mínimos en AWS

Este documento describe los pasos para crear un grupo en AWS con permisos mínimos, utilizando la política `AWSReadOnlyAccess`. Este grupo proporcionará acceso de solo lectura a los recursos de AWS, sin permitir cambios en ellos.

## Pasos para crear un grupo IAM con permisos mínimos

### 1. Accede a la Consola de AWS
- Abre tu [Consola de AWS](https://aws.amazon.com/console/).

### 2. Dirígete a IAM (Gestión de Identidad y Acceso)
- En la barra de búsqueda de la consola, escribe "IAM" y selecciona el servicio **IAM**.

### 3. Crear un Grupo
- En el menú de la izquierda, selecciona **Grupos**.
- Haz clic en el botón **Crear grupo**.

### 4. Nombrar el Grupo
- Nombra el grupo como **SecureAccess-Users** o cualquier nombre que prefieras para organizar el grupo.
  
### 5. Asignar Permisos
- En la lista de políticas, busca y selecciona la política **AWSReadOnlyAccess**.
  - Esta política otorga acceso de solo lectura a todos los recursos de AWS sin permitir realizar cambios.

### 6. Crear el Grupo
- Haz clic en el botón **Crear grupo** para finalizar la creación del grupo.

### 7. Confirmar el Grupo
- Una vez creado el grupo, puedes asignar usuarios a este para que tengan acceso con permisos de solo lectura.

## ¿Qué hace la política `AWSReadOnlyAccess`?
La política **AWSReadOnlyAccess** proporciona acceso de solo lectura a la mayoría de los servicios de AWS, permitiendo que los usuarios visualicen recursos pero no los modifiquen.

Este grupo es útil para situaciones donde se necesita monitorear y auditar recursos sin riesgo de cambios accidentales o maliciosos.

---

Si necesitas más información o asistencia adicional sobre cómo gestionar permisos en AWS IAM, consulta la [documentación oficial de AWS IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html).
