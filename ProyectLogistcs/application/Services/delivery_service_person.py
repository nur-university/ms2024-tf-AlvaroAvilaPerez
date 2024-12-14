from Infrastructure.repositories.delivery_person_repository import DeliveryPersonRepository
from domain.entities.delivery_person import DeliveryPerson
from domain.enums.zone import Zone
from domain.abstractions.base_entity import DeliveryPersonID


class DeliveryPersonService:
    def __init__(self):
        self.repository = DeliveryPersonRepository()

    def add_delivery_person(self, id: str, first_name: str, last_name: str, zone: Zone):
        delivery_person = DeliveryPerson(DeliveryPersonID(id), first_name, last_name, zone)
        return self.repository.add_delivery_person(delivery_person)

    def get_all_delivery_persons(self):
        return self.repository.get_all_delivery_persons()

    def delete_delivery_person(self, id: str):
        self.repository.delete_delivery_person(id)
