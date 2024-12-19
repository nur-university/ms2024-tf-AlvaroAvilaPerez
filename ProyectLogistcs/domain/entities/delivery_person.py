from domain.abstractions.id_generator import IDGenerator
from domain.enums.delivery_person_status import DeliveryPersonStatus
from domain.enums.zone import Zone


class DeliveryPerson:
    deleted_ids = set()  # Set to store deleted IDs
    counter = 1  # Counter for generating new IDs

    def __init__(self, first_name: str, last_name: str, zone: Zone, status: DeliveryPersonStatus = DeliveryPersonStatus.FREE, repository=None):
        self.id = self.create_new_id(repository)
        self.first_name = first_name
        self.last_name = last_name
        self.zone = zone
        self.status = status

    @staticmethod
    def create_new_id(repository=None) -> str:
        """Generates a new ID ensuring deleted IDs are not reused."""
        if repository:  # Use repository-based ID generation
            return IDGenerator.generate_id(repository, 'DP')
        while DeliveryPerson.counter in DeliveryPerson.deleted_ids:  # Skip deleted IDs
            DeliveryPerson.counter += 1
        formatted_id = str(DeliveryPerson.counter).zfill(3)  # Format: DP-001, DP-002, etc.
        DeliveryPerson.counter += 1
        return f"DP-{formatted_id}"