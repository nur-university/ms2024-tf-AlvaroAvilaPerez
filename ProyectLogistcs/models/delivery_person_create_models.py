from pydantic import BaseModel
from domain.enums.zone import Zone
from domain.enums.delivery_person_status import DeliveryPersonStatus

class DeliveryPersonCreateModel(BaseModel):
    first_name: str
    last_name: str
    zone: Zone
    status: DeliveryPersonStatus = DeliveryPersonStatus.FREE
