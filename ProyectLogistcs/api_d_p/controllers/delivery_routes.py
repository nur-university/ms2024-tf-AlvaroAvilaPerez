from fastapi import APIRouter, HTTPException
from typing import List
from models.delivery_create_model import DeliveryCreateModel
from models.delivery_response_model import DeliveryResponseModel
from application.Services.delivery_service import DeliveryService

router = APIRouter()
service = DeliveryService()

@router.post("/", response_model=DeliveryResponseModel)
def create_delivery(delivery: DeliveryCreateModel):
    """
    Crea una nueva entrega en la base de datos.
    """
    try:
        # Pass all fields from the delivery request, including id
        created_delivery = service.add_delivery(
            id=delivery.id,  # Ensure id is passed here
            person_id=delivery.person_id,
            package_id=delivery.package_id,
            client_name=delivery.client_name,
            delivery_date=delivery.delivery_date,
            address=delivery.address
        )
        return DeliveryResponseModel(
            id=created_delivery.id,
            person_id=created_delivery.person_id,
            package_id=created_delivery.package_id,
            client_name=created_delivery.client_name,
            delivery_date=created_delivery.delivery_date,
            address=created_delivery.address,
            status=created_delivery.status.value  # Assuming status is an enum
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=List[DeliveryResponseModel])
def read_deliveries():
    """
    Obtiene todas las entregas registradas en la base de datos.
    """
    deliveries = service.get_all_deliveries()
    return [
        DeliveryResponseModel(
            id=delivery.id,
            person_id=delivery.person_id,
            package_id=delivery.package_id,
            client_name=delivery.client_name,
            delivery_date=delivery.delivery_date,
            address=delivery.address,
            status=delivery.status.value
        ) for delivery in deliveries
    ]

@router.delete("/{delivery_id}", response_model=dict)
def delete_delivery(delivery_id: str):
    """
    Elimina una entrega de la base de datos.
    """
    try:
        service.delete_delivery(delivery_id)
        return {"detail": "Delivery deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
