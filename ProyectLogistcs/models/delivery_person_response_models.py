from pydantic import BaseModel
from domain.enums.zone import Zone

class DeliveryPersonResponseModel(BaseModel):
    id: str
    first_name: str
    last_name: str
    zone: Zone
    status: str
