import uuid
from datetime import date

from Infrastructure.repositories.delivery_repository import DeliveryRepository
from domain.entities.delivery import Delivery
from domain.enums.package_status import PackageStatus
from domain.abstractions.base_entity import DeliveryID


class DeliveryService:
    def __init__(self):
        self.repository = DeliveryRepository()

    def add_delivery(self, person_id: str, package_id: str, client_name: str, delivery_date: date,
                     address: str, id: str = None, status: PackageStatus = PackageStatus.PENDING):
        if not id:  # Si no se proporciona un ID, se genera uno automáticamente
            id = str(uuid.uuid4())

        delivery = Delivery(DeliveryID(id), person_id, package_id, client_name, delivery_date, address, status)
        return self.repository.add_delivery(delivery)

    def get_all_deliveries(self) -> list:
        return self.repository.get_all_deliveries()

    def delete_delivery(self, id: str) -> None:
        self.repository.delete_delivery(id)
