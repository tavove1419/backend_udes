# Sistema de Registro de Aspirantes

Backend desarrollado con Django y Django REST Framework para la gestión de preinscripciones, registro completo de aspirantes, validación de documentos y flujo de aprobación.

---

## Tecnologías utilizadas

- Python 3
- Django
- Django REST Framework
- JWT (SimpleJWT)
- PostgreSQL
- django-cors-headers
- Pillow

---

## Configuración del Proyecto

Para inicializar el proyecto correctamente, sigue estos pasos:

1. Clonar el repositorio  
2. Crear y activar el entorno virtual  
3. Instalar dependencias  
4. Configurar variables de entorno  
5. Ejecutar migraciones  
6. Levantar el servidor  

---

## Variables de Entorno

Crear un archivo `.env` en la raíz del proyecto con la siguiente configuración:

```env
# 🔹 Base de datos PostgreSQL
DB_NAME=nombre_base_datos
DB_USER=usuario_db
DB_PASSWORD=contraseña_db
DB_HOST=localhost
DB_PORT=5432

# 🔹 Django
SECRET_KEY=tu_clave_secreta
DEBUG=True

# 🔹 Configuración de envío de correos
EMAIL_HOST_USER=tu_correo@gmail.com
EMAIL_HOST_PASSWORD=clave_app_gmail

---

# CÓMO OTRO DEV LEVANTA TU PROYECTO

```bash
git clone ...
cd project

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

cp .env.example .env

python manage.py migrate
python manage.py runserver

