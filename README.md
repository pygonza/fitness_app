# RoutineTracker

RoutineTracker es una aplicación Django para el seguimiento de rutinas, ejercicios y sesiones de entrenamiento. Está diseñada con un enfoque en seguridad y despliegue flexible para entornos como PythonAnywhere y contenedores Docker.

## Funcionalidades principales

- Gestión de usuarios con autenticación y flujos de inicio/cierre de sesión.
- CRUD de ejercicios, rutinas y sesiones de entrenamiento.
- Dashboard con métricas de volumen y sesiones recientes.
- Control de acceso para que los usuarios vean solo sus propios datos.
- Soporte para manejo de configuración por variables de entorno.
- Static files optimizados con WhiteNoise para producción.

## Arquitectura

- Django 5.0
- Python 3.14
- Base de datos configurada mediante `dj-database-url`.
- Configuración de entorno mediante `python-decouple`.
- Frontend con plantillas Django y estilos tailwind-like.
- Despliegue con Gunicorn y WhiteNoise.

## Requisitos

- Python 3.12+ (se usa 3.14 en el desarrollo actual)
- pip
- virtualenv o entornos virtuales equivalentes
- Git

## Configuración local

1. Clonar el repositorio:

```bash
git clone <repositorio-url>
cd new_project2026
```

2. Crear un entorno virtual:

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

3. Instalar dependencias:

```bash
pip install --upgrade pip
pip install -r requirements/base.txt
```

4. Copiar el archivo de variables de entorno:

```bash
copy .env.example .env
```

5. Ajustar `.env` para el entorno local o de producción. Valores clave:

- `SECRET_KEY`: nunca subirlo al repositorio.
- `DEBUG`: `False` en producción.
- `ALLOWED_HOSTS`: configurar dominio o hosts válidos.
- `DATABASE_URL`: `sqlite:///db.sqlite3` para desarrollo o un string de base de datos para producción.
- `CSRF_TRUSTED_ORIGINS`: incluir `https://<dominio>` si se usa HTTPS.

6. Ejecutar migraciones:

```bash
python manage.py migrate
```

7. Crear un superusuario (opcional):

```bash
python manage.py createsuperuser
```

8. Recolectar archivos estáticos:

```bash
python manage.py collectstatic --noinput
```

9. Iniciar el servidor local:

```bash
python manage.py runserver
```

## Variables de entorno

El proyecto utiliza `python-decouple` y busca estas variables en `.env`:

- `SECRET_KEY`
- `DEBUG`
- `ALLOWED_HOSTS`
- `DATABASE_URL`
- `CSRF_TRUSTED_ORIGINS`
- `DEFAULT_FROM_EMAIL`

No debe subirse el archivo `.env` al repositorio. `.gitignore` ya excluye `.env`, `.venv`, `db.sqlite3`, y otros archivos locales.

## Despliegue en PythonAnywhere

1. Crear el entorno virtual en PythonAnywhere.
2. Clonar el repositorio en el directorio de tu cuenta.
3. Instalar dependencias:

```bash
pip install -r requirements/base.txt
```

4. Configurar el archivo `.env` con los valores de producción.
5. Ajustar `ALLOWED_HOSTS` para incluir el dominio de PythonAnywhere.
6. Ejecutar migraciones:

```bash
python manage.py migrate
```

7. Recolectar archivos estáticos:

```bash
python manage.py collectstatic --noinput
```

8. En la configuración del Web app de PythonAnywhere, establecer:

- `WSGI configuration file`: `routinetracker.config.wsgi`
- `DJANGO_SETTINGS_MODULE`: `routinetracker.config.settings`
- Entorno virtual: la ruta al `venv` creado.

## Despliegue con Docker

El proyecto incluye un `Dockerfile` y un `docker-compose.yml` para entornos de contenedor.

Para construir y ejecutar localmente:

```bash
docker-compose build
docker-compose up -d
```

La aplicación quedará disponible en `http://127.0.0.1:8000`.

## Seguridad

- Mantener `DEBUG=False` en producción.
- No almacenar `SECRET_KEY` ni credenciales en el repositorio.
- Apoyarse en `.env` para secretos y configuración sensible.
- Establecer valores válidos en `ALLOWED_HOSTS` y `CSRF_TRUSTED_ORIGINS`.
- Usar `STATIC_ROOT` y `collectstatic` para servir archivos estáticos en producción.
- Revisar las dependencias y actualizar regularmente.

## Pruebas

Ejecutar la suite de tests con:

```bash
pytest -q
```

El proyecto incluye pruebas unitarias para usuarios, ejercicios, rutinas y sesiones de entrenamiento.

## Buenas prácticas de GitHub

- No comprometer archivos locales o secretos.
- Confirmar solo los cambios necesarios.
- Usar mensajes de commit descriptivos.
- Verificar la aplicación local antes de hacer push.

## Resumen de archivos clave

- `manage.py` — punto de entrada de Django.
- `requirements/base.txt` — dependencias del proyecto.
- `routinetracker/config/settings.py` — configuración de Django.
- `templates/` — vistas de interfaz de usuario.
- `Dockerfile` y `docker-compose.yml` — despliegue en contenedores.
- `.env.example` — plantilla segura de variables de entorno.
- `.gitignore` — exclusiones para entornos locales y archivos sensibles.
