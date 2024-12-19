import unittest
from datetime import date
from domain.entities.delivery import Delivery
from domain.enums.package_status import PackageStatus
from domain.abstractions.base_id import DeliveryID


class TestDelivery(unittest.TestCase):

    def test_assign_to_person_positive(self):
        # Crear una instancia de Delivery en estado PENDING
        delivery = Delivery(
            id=DeliveryID("D001"),
            person_id="DP001",
            package_id="P001",
            client_name="Carlos López",
            delivery_date=date(2024, 12, 20),
            address="Av. América 456",
            status=PackageStatus.pending
        )

        # Asignar un repartidor
        delivery.assign_to_person("DP001")

        # Verificar que el repartidor fue asignado y el estado cambió a IN_PROGRESS
        self.assertEqual(delivery.person_id, "DP001")
        self.assertEqual(delivery.status, PackageStatus.pending)

    def test_assign_to_person_negative(self):
        # Crear una instancia de Delivery en estado COMPLETED
        delivery = Delivery(
            id=DeliveryID("D002"),
            person_id="DP123",
            package_id="P002",
            client_name="María Pérez",
            delivery_date=date(2024, 12, 22),
            address="Calle Bolívar 789",
            status=PackageStatus.completed
        )

        # Intentar asignar un repartidor debe lanzar un ValueError
        with self.assertRaises(ValueError) as context:
            delivery.assign_to_person("DP124")
        self.assertEqual(str(context.exception), "Cannot assign a delivery that has already been marked as completed.")
