from pydantic import BaseModel
from domain.enums.zone import Zone


# Modelo para la respuesta de datos
class DeliveryPersonResponseModels(BaseModel):
    id: str
    first_name: str
    last_name: str
    zone: Zone
    status: str