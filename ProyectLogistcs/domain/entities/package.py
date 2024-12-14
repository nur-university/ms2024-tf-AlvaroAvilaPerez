from datetime import date
from domain.enums.package_status import PackageStatus
from domain.abstractions.base_entity import PackageID


class Package:
    def __init__(self, id: PackageID, client_name: str, delivery_date: date, address: str):
        self.id = id
        self.client_name = client_name
        self.delivery_date = delivery_date
        self.address = address
        self.status = PackageStatus.PENDING

    def change_address(self, new_address: str):
        """Cambia la dirección de entrega."""
        self.address = new_address

    def mark_as_delivered(self):
        """Marca el paquete como entregado."""
        self.status = PackageStatus.DELIVERED