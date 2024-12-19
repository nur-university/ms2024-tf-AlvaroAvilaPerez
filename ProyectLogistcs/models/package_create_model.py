from pydantic import BaseModel
from datetime import date

class PackageCreateModel(BaseModel):
    client_id: str
    delivery_date: date

