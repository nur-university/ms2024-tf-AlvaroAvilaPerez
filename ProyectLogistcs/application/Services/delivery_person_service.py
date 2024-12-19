from Infrastructure.repositories.delivery_person_repository import DeliveryPersonRepository
from domain.entities.delivery_person import DeliveryPerson
from domain.enums.delivery_person_status import DeliveryPersonStatus
from domain.enums.zone import Zone


class DeliveryPersonService:
    def __init__(self):
        self.repository = DeliveryPersonRepository()

    def add_delivery_person(self, first_name: str, last_name: str, zone: Zone, status: DeliveryPersonStatus = DeliveryPersonStatus.FREE):
        delivery_person = DeliveryPerson(first_name, last_name, zone, status)
        return self.repository.add_delivery_person(delivery_person)

    def get_all_delivery_persons(self):
        return self.repository.get_all_delivery_persons()

    def delete_delivery_person(self, person_id: str):
        self.repository.delete_delivery_person(person_id)
