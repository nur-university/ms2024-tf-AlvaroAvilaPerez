from domain.abstractions.id_generator import IDGenerator
from domain.enums.plan import Plan


class Client:
    deleted_ids = set()  # Set to store deleted IDs
    counter = 1  # Counter for generating new IDs

    def __init__(self, first_name: str, last_name: str, address: str, plan: Plan, age: int, size: float, weight: float, repository=None):
        self.id = self.create_new_id() if repository is None else self.create_new_id(repository)
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.plan = plan
        self.age = age
        self.size = size
        self.weight = weight

    @staticmethod
    def create_new_id(repository=None):
        """Generates a new ID ensuring deleted IDs are not reused."""
        if repository:  # If a repository is provided, use the database ID generation system
            return IDGenerator.generate_id(repository, 'CL')
        else:
            # If there are deleted IDs, avoid reusing the smallest
            while Client.counter in Client.deleted_ids:
                Client.counter += 1  # Increment until finding an available one
            # Generates an ID with format CL-001, CL-002, CL-003, etc.
            formatted_id = str(Client.counter).zfill(3)  # Pads with leading zeros
            Client.counter += 1  # Increment the counter for the next ID
            return f"CL-{formatted_id}"