# Proyecto de Entregas

Este proyecto se encarga de gestionar las entregas de paquetes, asignación de personas de entrega, y el manejo de paquetes y entregas. A continuación se describen los pasos para instalar los requerimientos, levantar el servidor y ejemplos de cómo hacer `POST` para las entidades **Delivery Person**, **Packages** y **Deliveries**.

## Requisitos

1. Python 3.x
2. Pip
3. PostgreSQL (o cualquier base de datos que se configure para este proyecto)

## Instalación

1. Clonar el repositorio

   ```bash
   git clone <repositorio-url>
   cd <directorio-del-proyecto>
Crear un entorno virtual (opcional, pero recomendado)

```bash
Copy code
python3 -m venv venv
source venv/bin/activate  # En Windows usa venv\Scripts\activate
Instalar los requisitos
```

```bash
Copy code
pip install -r requirements.txt
Configuración de la base de datos
```
Asegúrate de tener la base de datos configurada y actualizada con los esquemas necesarios. Si es necesario, realiza las migraciones:

```bash
Copy code
python manage.py migrate
Levantar el servidor con Unicorn
```
Para inciar Unicorn como servidor ASGI.

```bash
Copy code
gunicorn main:app --reload
http://127.0.0.1:8000/docs
```
Endpoints
A continuación, se presentan ejemplos de cómo puedes realizar los POST para las siguientes entidades:

Delivery Person
POST /delivery_persons/

Cuerpo de la solicitud:
```bash
json
Copy code
{
  "id": "DP004",
  "first_name": "Carlos Antonio",
  "last_name": "Lalo Tudela",
  "zone": "Central",
  "status": "Free"
}
```
Packages
POST /packages/

Cuerpo de la solicitud:
```bash
json
Copy code
{
  "id": "P004",
  "client_name": "María Elena Rodríguez Álvarez",
  "delivery_date": "2024-12-14",
  "address": "Calle Ayacucho, Centro, Cochabamba",
  "status": "Pending"
}
```
Deliveries
POST /deliveries/

Cuerpo de la solicitud:
```bash
json
Copy code
{
  "id": "D002",
  "person_id": "PS002",
  "package_id": "P002",
  "client_name": "Ana María Gutiérrez Salazar",
  "delivery_date": "2024-12-14T00:00:00",
  "address": "Calle Ayacucho, Centro, Cochabamba",
  "status": "Pending"
}
```
Ejemplo de estructura de datos
Delivery Person
```bash
json
Copy code
[
  {
    "id": "string",
    "first_name": "string",
    "last_name": "string",
    "zone": "Central",
    "status": "string"
  }
]
```
Ejemplo:
```bash
json
Copy code
{
  "id": "DP004",
  "first_name": "Carlos Antonio",
  "last_name": "Lalo Tudela",
  "zone": "Central",
  "status": "Free"
}
```
Packages
```bash
json
Copy code
[
  {
    "id": "string",
    "client_name": "string",
    "delivery_date": "2024-12-13",
    "address": "string",
    "status": "Pending"
  }
]
```
Ejemplo:
```bash
json
Copy code
{
  "id": "P004",
  "client_name": "María Elena Rodríguez Álvarez",
  "delivery_date": "2024-12-14",
  "address": "Calle Ayacucho, Centro, Cochabamba",
  "status": "Pending"
}
```
Deliveries
```bash
json
Copy code
{
  "id": "string",
  "person_id": "string",
  "package_id": "string",
  "client_name": "string",
  "delivery_date": "2024-12-13T23:33:09.266Z",
  "address": "string",
  "status": "Pending"
}
```
Ejemplo:
```bash
json
Copy code
{
  "id": "D002",
  "person_id": "PS002",
  "package_id": "P002",
  "client_name": "Ana María Gutiérrez Salazar",
  "delivery_date": "2024-12-14T00:00:00",
  "address": "Calle Ayacucho, Centro, Cochabamba",
  "status": "Pending"
}
```