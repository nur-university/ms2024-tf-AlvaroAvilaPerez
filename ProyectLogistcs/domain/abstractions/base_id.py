from abc import ABC, abstractmethod

from domain.abstractions.id_generator import IDGenerator



class AbstractID(ABC):
    @abstractmethod
    def __str__(self):
        pass

class DeliveryPersonID(AbstractID):
    def __init__(self, id: str):
        self.id = id

    def __str__(self):
        return self.id

class PackageID(AbstractID):
    def __init__(self, id: str):
        self.id = id

    def __str__(self):
        return self.id

class DeliveryID(AbstractID):
    def __init__(self, id: str):
        self.id = id

    def __str__(self):
        return self.id

class ClientID(AbstractID):
    def __init__(self, id: str):
        self.id = id

    def __str__(self):
        return self.id