from datetime import date
from domain.abstractions.id_generator import IDGenerator
from domain.enums.package_status import PackageStatus


class Package:
    deleted_ids = set()
    counter = 1

    def __init__(self, client_id: str, delivery_date: date, repository=None):
        self.id = self.create_new_id(repository)
        self.client_id = client_id
        self.delivery_date = delivery_date
        self.status = PackageStatus.pending

    @staticmethod
    def create_new_id(repository=None):
        """Generates a new ID ensuring that deleted IDs are not reused."""
        if repository:
            return IDGenerator.generate_id(repository, 'PK')
        else:
            while Package.counter in Package.deleted_ids:
                Package.counter += 1
            formatted_id = str(Package.counter).zfill(3)
            Package.counter += 1
            return f"PK-{formatted_id}"
