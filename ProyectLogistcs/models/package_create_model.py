from datetime import date

from pydantic import BaseModel


class PackageCreateModel(BaseModel):
    client_name: str
    delivery_date: date = date.today()
    address: str