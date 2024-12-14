from datetime import date

from domain.enums.delivery_status import DeliveryStatus
from domain.enums.package_status import PackageStatus
from domain.abstractions.base_entity import DeliveryID


class Delivery:
    def __init__(self, id: DeliveryID, person_id: str, package_id: str, client_name: str, delivery_date: date,
                 address: str, status: DeliveryStatus = DeliveryStatus.pending):
        self.id = id  # ID de la entrega
        self.person_id = person_id  # ID del repartidor
        self.package_id = package_id  # ID del paquete
        self.client_name = client_name  # Nombre del cliente
        self.delivery_date = delivery_date  # Fecha de entrega
        self.address = address  # Dirección de entrega
        self.status = status  # Estado de la entrega (por defecto es PENDING)

    def mark_as_delivered(self):
        """Marca la entrega como completada."""
        self.status = PackageStatus.DELIVERED

    def assign_to_person(self, person_id: str):
        """
        Asigna esta entrega a un repartidor y actualiza el estado a IN_PROGRESS.
        """
        if self.status == DeliveryStatus.completed:
            raise ValueError("Cannot assign a delivery that has already been marked as completed.")
        if not person_id or not isinstance(person_id, str):
            raise ValueError("Invalid person ID provided.")

    def __repr__(self):
        return f"<Delivery(id={self.id}, person_id={self.person_id}, package_id={self.package_id}, client_name={self.client_name}, delivery_date={self.delivery_date}, address={self.address}, status={self.status})>"