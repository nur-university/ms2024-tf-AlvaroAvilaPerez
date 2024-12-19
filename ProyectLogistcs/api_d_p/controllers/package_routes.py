from fastapi import APIRouter, HTTPException
from typing import List
from models.package_create_model import PackageCreateModel
from models.package_response_model import PackageResponseModel
from application.Services.package_service import PackageService

router = APIRouter()
service_package = PackageService()

@router.post("/", response_model=PackageResponseModel)
def create_package(package: PackageCreateModel):
    try:
        created_package = service_package.add_package(
            client_id=package.client_id,
            delivery_date=package.delivery_date,
        )
        client = created_package.client
        return PackageResponseModel(
            id=str(created_package.id),
            client_id=created_package.client_id,
            first_name=client.first_name,
            last_name=client.last_name,
            delivery_date=created_package.delivery_date,
            address=client.address,
            status=created_package.status  # Ensure the status field is included here
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[PackageResponseModel])
def read_packages():
    try:
        packages = service_package.get_all_packages()
        return [
            PackageResponseModel(
                id=str(package.id),
                client_id=package.client_id,  # Ensure client_id is in the response
                first_name=package.client.first_name,
                last_name=package.client.last_name,
                delivery_date=package.delivery_date,
                address=package.client.address,
                status=package.status,
            ) for package in packages
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error retrieving packages: " + str(e))

@router.delete("/{package_id}", response_model=dict)
def delete_package(package_id: str):
    try:
        service_package.delete_package(package_id)
        return {"detail": "Package deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail="Package not found: " + str(e))

