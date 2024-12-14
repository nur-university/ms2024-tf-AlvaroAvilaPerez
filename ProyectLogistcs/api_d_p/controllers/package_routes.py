from fastapi import APIRouter, HTTPException
from typing import List
from models.package_create_model import PackageCreateModel
from models.package_response_model import PackageResponseModel
from application.Services.package_service import PackageService

router = APIRouter()
service = PackageService()

@router.post("/", response_model=PackageResponseModel)
def create_package(package: PackageCreateModel):
    """
    Crea un nuevo paquete en la base de datos.
    """
    try:
        created_package = service.add_package(
            client_name=package.client_name,
            delivery_date=package.delivery_date,
            address=package.address
        )
        return PackageResponseModel(
            id=created_package.id,
            client_name=created_package.client_name,
            delivery_date=created_package.delivery_date,
            address=created_package.address,
            status=created_package.status.value
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[PackageResponseModel])
def read_packages():
    """
    Obtiene todos los paquetes registrados en la base de datos.
    """
    packages = service.get_all_packages()
    return [
        PackageResponseModel(
            id=package.id,
            client_name=package.client_name,
            delivery_date=package.delivery_date,
            address=package.address,
            status=package.status.value
        ) for package in packages
    ]

@router.delete("/{package_id}", response_model=dict)
def delete_package(package_id: str):
    """
    Elimina un paquete de la base de datos.
    """
    try:
        service.delete_package(package_id)
        return {"detail": "Package deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
