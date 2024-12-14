from pydantic import BaseModel
from domain.enums.zone import Zone


# Modelo para la entrada de datos
class DeliveryPersonCreateModels(BaseModel):
    id: str
    first_name: str
    last_name: str
    zone: Zone

