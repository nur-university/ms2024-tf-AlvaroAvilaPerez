from domain.enums.delivery_person_status import DeliveryPersonStatus
from domain.enums.zone import Zone
from domain.abstractions.base_entity import DeliveryPersonID


class DeliveryPerson:
    def __init__(self, id: DeliveryPersonID, first_name: str, last_name: str, zone: Zone, status: DeliveryPersonStatus = DeliveryPersonStatus.FREE):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.zone = zone
        self.status = status
        self.assigned_deliveries = []  # Inicializa el atributo 'assigned_deliveries' como lista vacía


    def set_status(self, status: DeliveryPersonStatus):
        self.status = status

    def assign_delivery(self, delivery_id: str):
        """Asignar un pedido al repartidor, pero solo si tiene menos de 3 asignaciones pendientes."""
        if len(self.assigned_deliveries) >= 3:
            raise ValueError("Cannot assign more than 3 pending deliveries to a delivery person.")
        self.assigned_deliveries.append(delivery_id)

    def get_assigned_deliveries(self):
        """Devuelve la lista de entregas asignadas."""
        return self.assigned_deliveries