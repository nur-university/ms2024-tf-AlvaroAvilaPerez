from fastapi import APIRouter, HTTPException
from typing import List

from application.Services.delivery_person_service import DeliveryPersonService
from models.delivery_person_create_models import DeliveryPersonCreateModel
from models.delivery_person_response_models import DeliveryPersonResponseModel

router = APIRouter()
service_delivery_person = DeliveryPersonService()


@router.post("/", response_model=DeliveryPersonResponseModel)
def create_delivery_person(delivery_person: DeliveryPersonCreateModel):
    try:
        created_delivery_person = service_delivery_person.add_delivery_person(
            first_name=delivery_person.first_name,
            last_name=delivery_person.last_name,
            zone=delivery_person.zone,
            status=delivery_person.status  # Defaults to FREE if not provided
        )
        return DeliveryPersonResponseModel(
            id=str(created_delivery_person.id),
            first_name=created_delivery_person.first_name,
            last_name=created_delivery_person.last_name,
            zone=created_delivery_person.zone,
            status=created_delivery_person.status
        )
    except Exception as e:
        # Log the error (optional: integrate with a logging framework)
        raise HTTPException(
            status_code=400,
            detail=f"Failed to create delivery person: {str(e)}"
        )


@router.get("/", response_model=List[DeliveryPersonResponseModel])
def read_delivery_persons():
    try:
        persons = service_delivery_person.get_all_delivery_persons()
        return [
            DeliveryPersonResponseModel(
                id=str(person.id),
                first_name=person.first_name,
                last_name=person.last_name,
                zone=person.zone,
                status=person.status
            ) for person in persons
        ]
    except Exception as e:
        # Log the error (optional)
        raise HTTPException(
            status_code=500,
            detail="Error retrieving delivery persons"
        )


@router.delete("/{person_id}", response_model=dict)
def delete_delivery_person(person_id: str):
    try:
        service_delivery_person.delete_delivery_person(person_id)
        return {"detail": "Delivery person deleted successfully"}
    except KeyError:  # Handle specific repository exceptions
        raise HTTPException(
            status_code=404,
            detail=f"Delivery person with ID {person_id} not found"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error deleting delivery person: {str(e)}"
        )
