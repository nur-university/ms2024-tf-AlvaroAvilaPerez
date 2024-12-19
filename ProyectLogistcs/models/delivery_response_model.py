from datetime import date

from pydantic import BaseModel


class DeliveryResponseModel(BaseModel):
    id: str
    package_id: str
    client_id: str
    first_name: str
    last_name: str
    delivery_date: date
    address: str
    person_delivery_id: str
    status: str
