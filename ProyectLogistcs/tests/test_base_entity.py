import pytest

from domain.abstractions.base_id import AbstractID, DeliveryPersonID, PackageID, DeliveryID


# Pruebas
def test_abstract_id_cannot_be_instantiated():
    """Verifica que AbstractID no se pueda instanciar directamente"""
    with pytest.raises(TypeError):
        AbstractID()

def test_delivery_person_id():
    """Verifica la funcionalidad de DeliveryPersonID"""
    id_value = "DP123"
    delivery_person_id = DeliveryPersonID(id_value)
    assert str(delivery_person_id) == id_value
    assert isinstance(delivery_person_id, AbstractID)

def test_package_id():
    """Verifica la funcionalidad de PackageID"""
    id_value = "PK456"
    package_id = PackageID(id_value)
    assert str(package_id) == id_value
    assert isinstance(package_id, AbstractID)

def test_delivery_id():
    """Verifica la funcionalidad de DeliveryID"""
    id_value = "DL789"
    delivery_id = DeliveryID(id_value)
    assert str(delivery_id) == id_value
    assert isinstance(delivery_id, AbstractID)