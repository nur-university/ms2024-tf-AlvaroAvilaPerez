import unittest
from datetime import datetime

from domain.abstractions.base_entity import DeliveryPersonID
from domain.entities.delivery_person import DeliveryPerson
from domain.enums.zone import Zone


class TestDeliveryPerson(unittest.TestCase):

    def test_assign_delivery_to_delivery_person_with_or_without_assigned_deliveries(self):
        # Crear un repartidor
        delivery_person = DeliveryPerson(DeliveryPersonID("DP001"), "Juan", "Pérez", Zone("Central"))

        # Asignar tres entregas
        delivery_person.assign_delivery("D001")
        delivery_person.assign_delivery("D002")
        delivery_person.assign_delivery("D003")

        # Verificar que las tres entregas fueron asignadas
        self.assertEqual(delivery_person.get_assigned_deliveries(), ["D001", "D002", "D003"])

    def test_assign_delivery_to_delivery_person_with_all_assigned_deliveries(self):
        # Crear un repartidor con tres entregas asignadas
        delivery_person = DeliveryPerson(DeliveryPersonID("DP001"), "Juan", "Pérez", Zone("Central"))
        delivery_person.assign_delivery("D001")
        delivery_person.assign_delivery("D002")
        delivery_person.assign_delivery("D003")

        # Intentar asignar una cuarta entrega debe lanzar un ValueError
        with self.assertRaises(ValueError):
            delivery_person.assign_delivery("D004")