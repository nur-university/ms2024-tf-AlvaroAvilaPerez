from fastapi import APIRouter, HTTPException
from typing import List
from models.client_create_model import ClientCreateModel
from models.client_response_model import ClientResponseModel
from application.Services.client_service import ClientService

router = APIRouter()
service_client = ClientService()

@router.post("/", response_model=ClientResponseModel)
def create_client(client: ClientCreateModel):
    try:
        created_client = service_client.add_client(
            first_name=client.first_name,
            last_name=client.last_name,
            address=client.address,
            plan=client.plan,
            age=client.age,
            size=client.size,
            weight=client.weight
        )
        return ClientResponseModel(
            id=str(created_client.id),
            first_name=created_client.first_name,
            last_name=created_client.last_name,
            address=created_client.address,
            plan=created_client.plan,
            age=created_client.age,
            size=created_client.size,
            weight=created_client.weight
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[ClientResponseModel])
def read_clients():
    try:
        clients = service_client.get_all_clients()
        return [
            ClientResponseModel(
                id=str(client.id),
                first_name=client.first_name,
                last_name=client.last_name,
                address=client.address,
                plan=client.plan,
                age=client.age,
                size=client.size,
                weight=client.weight
            ) for client in clients
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error retrieving clients: " + str(e))

@router.delete("/{client_id}", response_model=dict)
def delete_client(client_id: str):
    try:
        service_client.delete_client(client_id)
        return {"detail": "Client deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail="Client not found: " + str(e))
