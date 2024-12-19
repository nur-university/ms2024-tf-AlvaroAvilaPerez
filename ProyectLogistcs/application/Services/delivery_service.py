from Infrastructure.repositories.delivery_person_repository import DeliveryPersonRepository
from Infrastructure.repositories.delivery_repository import DeliveryRepository
from Infrastructure.repositories.package_repository import PackageRepository
from domain.entities.delivery import Delivery
from domain.enums.package_status import PackageStatus


class DeliveryService:
    def __init__(self):
        self.repository = DeliveryRepository()
        self.package_repository = PackageRepository()
        self.delivery_person_repository = DeliveryPersonRepository()

    def add_delivery(self, package_id: str, delivery_person_id: str):
        package = self.package_repository.get_package_by_id(package_id)
        if not package:
            raise ValueError("Package not found")

        delivery_person = self.delivery_person_repository.get_delivery_person_by_id(delivery_person_id)
        if not delivery_person:
            raise ValueError("Delivery person not found")

        if not delivery_person.status:
            raise ValueError("Delivery person is not available")

        delivery = Delivery(
            package_id=package_id,
            delivery_person_id=delivery_person_id,
        )

        return self.repository.add_delivery(delivery)

    def get_all_deliveries(self) -> list:
        return self.repository.get_all_delivery()

    def delete_delivery(self, delivery_id: str) -> None:
        self.repository.delete_delivery(delivery_id)

    def update_package_status(self, delivery_id: str, status: str):
        try:
            try:
                status_enum = PackageStatus(status)
            except ValueError:
                raise ValueError("Invalid status")

            delivery = self.repository.get_delivery_by_id(delivery_id)
            if not delivery:
                raise ValueError("Delivery not found")

            package = delivery.package
            if not package:
                raise ValueError("Package not found for this delivery")

            package.status = status_enum.value

            self.package_repository.update_package(package)
            return package

        except Exception as e:
            raise ValueError(f"Error updating package status: {str(e)}")