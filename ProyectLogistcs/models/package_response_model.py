from datetime import date

from pydantic import BaseModel

from domain.enums.package_status import PackageStatus


class PackageResponseModel(BaseModel):
    id: str
    client_name: str
    delivery_date: date
    address: str
    status: PackageStatus