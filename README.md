# Proyecto de Entregas

Este proyecto se encarga de gestionar las entregas de paquetes, asignación de personas de entrega y el manejo de paquetes y entregas. A continuación se describen los pasos para instalar los requerimientos, levantar el servidor y ejemplos de cómo hacer solicitudes `POST` para las entidades **Delivery Person**, **Packages** y **Deliveries**.

## Requisitos

1. **Python 3.x**
2. **Pip** - Para la gestión de dependencias.
3. **PostgreSQL** (o cualquier base de datos que se configure para este proyecto).

## Pasos de Instalación

1. **Seleccionar el intérprete de Python**: 
   Asegúrate de que tu entorno esté configurado para usar la versión de Python 3.x que necesitas. Esto se puede hacer en tu IDE o terminal utilizando herramientas como `pyenv`.

2. **Instalar los requerimientos**:
   Ejecuta el siguiente comando para instalar las dependencias necesarias para el proyecto:
   
   ```bash
   pip install -r requirements.txt
Iniciar el servidor: Usa uvicorn para levantar el servidor de desarrollo de FastAPI. Ejecuta el siguiente comando:

  ```bash
uvicorn main:app --reload
```
El servidor estará disponible en http://127.0.0.1:8000/docs, donde podrás realizar consultas a la API.