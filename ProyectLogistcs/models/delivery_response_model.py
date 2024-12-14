from pydantic import BaseModel
from datetime import datetime

class DeliveryResponseModel(BaseModel):
    id: str
    person_id: str
    package_id: str
    client_name: str
    delivery_date: datetime
    address: str
    status: str

