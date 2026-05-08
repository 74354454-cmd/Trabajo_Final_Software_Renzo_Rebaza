# 🔁 Conversor de Unidades - Evaluación Final

Este es el proyecto final individual desarrollado para la asignatura de **Construcción de Software**. La aplicación es un sistema de conversión de unidades que incluye una interfaz web, persistencia en base de datos y despliegue con Docker.

---

## 🚀 Tecnologías Utilizadas
* **Backend**: Flask (Python 3.14).
* **Base de Datos**: SQLAlchemy con SQLite para el historial.
* **DevOps**: Docker para la portabilidad.
* **Pruebas**: Pytest para asegurar que las conversiones sean correctas.

---

## 🛠️ Cómo ejecutar el proyecto

### Ejecución con Python
1. Instala las librerías: `pip install flask sqlalchemy`.
2. Inicia la app: `python app.py`.

### Ejecución con Docker 🐳
1. Construye la imagen: `docker build -t conversor-final .`.
2. Inicia el contenedor: `docker run -p 5000:5000 conversor-final`.

---

## 👤 Autor
* **Renzo Rebaza Quequezana** - Trabajo Individual.