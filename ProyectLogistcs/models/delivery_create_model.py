from pydantic import BaseModel


class DeliveryCreateModel(BaseModel):
    package_id: str
    delivery_person_id: str
