from Infrastructure.repositories.client_repository import ClientRepository
from domain.entities.client import Client
from domain.enums.plan import Plan


class ClientService:
    def __init__(self):
        self.repository = ClientRepository()

    def add_client(self, first_name: str, last_name: str, address: str, plan: Plan, age: int, size: float, weight: float):
        client = Client(first_name, last_name, address, plan, age, size, weight)
        return self.repository.add_client(client)

    def get_all_clients(self):
        return self.repository.get_all_clients()

    def delete_client(self, client_id: str):
        self.repository.delete_client(client_id)
