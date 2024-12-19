from typing import List
from fastapi import APIRouter, HTTPException
from application.Services.delivery_service import DeliveryService
from models.delivery_create_model import DeliveryCreateModel
from models.delivery_response_model import DeliveryResponseModel

router = APIRouter()
service_delivery = DeliveryService()

@router.post("/", response_model=DeliveryResponseModel)
def create_delivery(delivery: DeliveryCreateModel):
    try:
        created_delivery = service_delivery.add_delivery(
            package_id=delivery.package_id,
            delivery_person_id=delivery.delivery_person_id,
        )
        package = created_delivery.package
        delivery_person = created_delivery.delivery_person
        return DeliveryResponseModel(
            id=str(created_delivery.id),
            package_id=created_delivery.package_id,
            client_id=package.client.id,
            first_name=package.client.first_name,
            last_name=package.client.last_name,
            delivery_date=package.delivery_date,
            address=package.client.address,
            person_delivery_id=created_delivery.delivery_person_id,
            status=package.status,
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[DeliveryResponseModel])
def read_deliveries():
    try:
        deliveries = service_delivery.get_all_deliveries()
        return [
            DeliveryResponseModel(
                id=str(delivery.id),
                package_id=delivery.package_id,
                client_id=delivery.package.client.id,
                first_name=delivery.package.client.first_name,
                last_name=delivery.package.client.last_name,
                delivery_date=delivery.package.delivery_date,
                address=delivery.package.client.address,
                person_delivery_id=delivery.delivery_person_id,
                status=delivery.package.status,
            )
            for delivery in deliveries
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error retrieving deliveries: " + str(e))


@router.delete("/{delivery_id}", response_model=dict)
def delete_delivery(delivery_id: str):
    try:
        service_delivery.delete_delivery(delivery_id)
        return {"detail": "Delivery deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail="Delivery not found: " + str(e))


@router.patch("/{delivery_id}/status", response_model=dict)
def update_package_status(delivery_id: str, status: str):
    try:
        service_delivery.update_package_status(delivery_id, status)
        return {"detail": f"Package status updated to '{status}' successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
