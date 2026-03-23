Para inicializar el proyecto es necesario que despues de instalados los paquetes y creado el entorno virtual,
crear el archivo .env y agregar las variables solicitadad

Variables de Entorno

DB_NAME=Nombre de la base de datos en postgresql
DB_USER=Usuario de la base de datos
DB_PASSWORD=contraseña
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=
DEBUG=True


#DATA PARA ENVIO DE EMAILS
EMAIL_HOST_USER=su correo electronico
EMAIL_HOST_PASSWORD=clave app gmail para el envio de correo

Es necesario que sea configurado un correo con los permisos pertinentes para enviar email desde el proyecto
en caso de usar uno de gmail realizar la configuración y permisos para obter la clave que permitar el envio de correos

