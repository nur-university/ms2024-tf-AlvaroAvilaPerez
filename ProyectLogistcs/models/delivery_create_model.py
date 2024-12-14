from pydantic import BaseModel
from datetime import datetime

from domain.enums.package_status import PackageStatus


class DeliveryCreateModel(BaseModel):
    id: str  # Este campo es obligatorio
    person_id: str
    package_id: str
    client_name: str
    delivery_date: datetime
    address: str
    status: PackageStatus = PackageStatus.PENDING
