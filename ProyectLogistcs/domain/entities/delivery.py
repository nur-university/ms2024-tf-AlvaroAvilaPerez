from domain.abstractions.id_generator import IDGenerator


class Delivery:
    deleted_ids = set()
    counter = 1

    def __init__(self, package_id: str, delivery_person_id: str, repository=None):
        self.id = self.create_new_id(repository)
        self.package_id = package_id
        self.delivery_person_id = delivery_person_id

    @staticmethod
    def create_new_id(repository=None):
        """Generates a new ID ensuring that deleted IDs are not reused."""
        if repository:
            return IDGenerator.generate_id(repository, 'D')
        else:
            while Delivery.counter in Delivery.deleted_ids:
                Delivery.counter += 1
            formatted_id = str(Delivery.counter).zfill(3)
            Delivery.counter += 1
            return f"D-{formatted_id}"
