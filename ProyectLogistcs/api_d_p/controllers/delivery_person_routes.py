from fastapi import APIRouter, HTTPException
from typing import List
from models.delivery_person_create_models import DeliveryPersonCreateModels
from models.delivery_person_response_models import DeliveryPersonResponseModels
from application.Services.delivery_service_person import DeliveryPersonService


router = APIRouter()
service = DeliveryPersonService()

@router.post("/", response_model=DeliveryPersonResponseModels)
def create_delivery_person(delivery_person: DeliveryPersonCreateModels):
    """
    Crea un nuevo repartidor en la base de datos.

    :param delivery_person: Datos del repartidor a crear.
    :return: Repartidor creado.
    """
    try:
        created_person = service.add_delivery_person(
            id=delivery_person.id,
            first_name=delivery_person.first_name,
            last_name=delivery_person.last_name,
            zone=delivery_person.zone
        )
        return DeliveryPersonResponseModels(
            id=created_person.id,
            first_name=created_person.first_name,
            last_name=created_person.last_name,
            zone=created_person.zone,
            status=created_person.status.value
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[DeliveryPersonResponseModels])
def read_delivery_persons():
    """
    Obtiene todos los repartidores registrados en la base de datos.

    :return: Lista de repartidores.
    """
    persons = service.get_all_delivery_persons()
    return [
        DeliveryPersonResponseModels(
            id=person.id,
            first_name=person.first_name,
            last_name=person.last_name,
            zone=person.zone,
            status=person.status.value
        ) for person in persons
    ]

@router.delete("/{delivery_person_id}", response_model=dict)
def delete_delivery_person(delivery_person_id: str):
    """
    Elimina un repartidor de la base de datos.

    :param delivery_person_id: ID del repartidor a eliminar.
    :return: Mensaje de éxito.
    """
    try:
        service.delete_delivery_person(delivery_person_id)
        return {"detail": "Delivery person deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

