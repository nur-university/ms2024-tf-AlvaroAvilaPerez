from datetime import date
from Infrastructure.repositories.package_repository import PackageRepository
from domain.entities.package import Package
from domain.abstractions.base_entity import PackageID


class PackageService:
    def __init__(self):
        self.repository = PackageRepository()

    def add_package(self, client_name: str, delivery_date: date, address: str):
        """Crea un nuevo paquete y lo agrega a la base de datos."""
        package_id = self.generate_package_id()
        package = Package(PackageID(package_id), client_name, delivery_date, address)
        return self.repository.add_package(package)

    def generate_package_id(self) -> str:
        """Genera un nuevo ID de paquete en formato PXXX, donde XXX es un número correlativo."""
        last_package = self.repository.get_last_package()
        if last_package:
            last_id = int(last_package.id[1:])  # Extrae el número del ID
            new_id = f"P{last_id + 1:03d}"  # Genera el nuevo ID
        else:
            new_id = "P001"  # Primer ID
        return new_id

    def get_all_packages(self):
        """Obtiene todos los paquetes registrados en la base de datos."""
        return self.repository.get_all_packages()

    def delete_package(self, package_id: str):
        """Elimina un paquete de la base de datos."""
        self.repository.delete_package(package_id)
