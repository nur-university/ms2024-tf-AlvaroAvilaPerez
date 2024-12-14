import unittest
from datetime import datetime
from domain.entities.delivery import Delivery
from domain.entities.address import Address
from application.Services.route_optimization_service import RouteOptimizationService

class TestRouteOptimizationService(unittest.TestCase):

    def test_optimize_routes(self):
        # Pasando un objeto Address con zona correctamente definida
        delivery1 = Delivery(1, "Juan Carlos", "12345", "Juan Carlos", datetime(2024, 12, 15, 10, 0).date(),
                             Address("Avenida Heroínas", "Cochamba", "central"))
        delivery2 = Delivery(2, "María Fernanda", "12346", "María Fernanda", datetime(2024, 12, 15, 11, 0).date(),
                             Address("Avenida Villarroel", "Cochamba", "north"))
        delivery3 = Delivery(3, "Luis Alberto", "12347", "Luis Alberto", datetime(2024, 12, 15, 12, 0).date(),
                             Address("Villa Primero mayo", "Cochamba", "south"))

        deliveries = [delivery2, delivery3, delivery1]
        optimized_deliveries = RouteOptimizationService.optimize_routes(deliveries)

        # Asegúrate de que las entregas estén optimizadas según la prioridad de la ruta
        self.assertEqual(optimized_deliveries[0], delivery1)  # central tiene la prioridad más alta (1)
        self.assertEqual(optimized_deliveries[1], delivery2)  # north tiene la siguiente prioridad (2)
        self.assertEqual(optimized_deliveries[2], delivery3)  # south tiene la prioridad más baja (3)

