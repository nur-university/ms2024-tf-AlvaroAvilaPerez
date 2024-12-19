from datetime import date

from Infrastructure.repositories.client_repository import ClientRepository
from Infrastructure.repositories.package_repository import PackageRepository
from domain.entities.package import Package


class PackageService:
    def __init__(self):
        self.repository = PackageRepository()
        self.client_repository = ClientRepository()

    def add_package(self, client_id: str, delivery_date: date):
        client = self.client_repository.get_client_by_id(client_id)
        if not client:
            raise ValueError("Client not found")

        package = Package(
            client_id=client_id,
            delivery_date=delivery_date,
        )
        return self.repository.add_package(package)

    def get_all_packages(self):
        """Fetch all packages without the status."""
        return self.repository.get_all_packages()

    def delete_package(self, package_id: str):
        """Deletes a package from the database."""
        self.repository.delete_package(package_id)
