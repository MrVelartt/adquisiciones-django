# 🛠️ Backend – Gestión de Adquisiciones (Django REST)

Este es el backend desarrollado con **Django 5** y **Django Rest Framework (DRF)** para gestionar adquisiciones en una organización. Expone una API RESTful robusta que permite crear, listar, filtrar y versionar registros de adquisiciones. Además, ofrece documentación automática con Swagger e integración con una base de datos SQL Server.

---

## 🌐 Tecnologías Utilizadas

- Django 5  
- Django Rest Framework (DRF)  
- Python 3.11+  
- SQL Server (con conector ODBC Driver 17)  
- Swagger/OpenAPI  
- Django Reversion (historial de cambios)  
- CORS Headers (para integración con frontend Angular)  

---

## 🎯 Funcionalidades Principales

- ✅ API RESTful para operaciones CRUD de adquisiciones  
- 🔐 Seguridad base con middleware y control de acceso  
- 🔍 Filtros avanzados por proveedor, tipo, fecha y más  
- ♻️ **Historial de cambios automático** gracias a `django-reversion`  
- 📄 Documentación interactiva vía **Swagger** (`drf-spectacular`)  
- ⚙️ Serialización, validaciones y paginación  
- 🌍 CORS habilitado para integración directa con el frontend Angular  

---

## ⚙️ Configuración de Base de Datos (SQL Server)

Este proyecto está conectado a una base de datos Microsoft SQL Server mediante el backend `mssql` y ODBC Driver 17. La configuración se define en el archivo `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'django-sqlserver',
        'USER': 'sa',
        'PASSWORD': 'Voluntad1',
        'HOST': 'VELARTT\\SQLSERVER',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'trust_server_certificate': 'yes',
        },
    }
}
```

> Asegúrate de tener instalado el driver ODBC 17 para SQL Server y configurado el alias del servidor correctamente (`VELARTT\\SQLSERVER`).

---

## ▶️ Instalación y Ejecución

1. Clona el repositorio:

```bash
git clone https://github.com/MrVelartt/adquisiciones-django.git
cd adquisiciones-backend
```

2. Crea y activa un entorno virtual:

```bash
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
```

3. Instala dependencias:

```bash
pip install -r requirements.txt
```

4. Aplica migraciones:

```bash
python manage.py migrate
```

5. Crea un superusuario (opcional):

```bash
python manage.py createsuperuser
```

6. Ejecuta el servidor:

```bash
python manage.py runserver
```

La API estará disponible en:  
[http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)

La documentación Swagger estará en:  
[http://127.0.0.1:8000/api/swagger

---

## 📚 Notas Adicionales

- La gestión de historial de adquisiciones se realiza automáticamente mediante `django-reversion`. Cada modificación queda registrada.
- Se incluye compatibilidad con Angular (CORS activado).
- Puedes extender el sistema de autenticación con JWT o permisos avanzados según los roles.

