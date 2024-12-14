import unittest

from domain.entities.address import Address


class TestAddress(unittest.TestCase):

    def test_calculate_route_priority(self):
        address1 = Address("123 Main St", "CityA", "central")
        address2 = Address("456 Elm St", "CityB", "north")
        address3 = Address("789 Oak St", "CityC", "south")
        address4 = Address("101 Pine St", "CityD", "unknown")

        self.assertEqual(address1.calculate_route_priority(), 1)
        self.assertEqual(address2.calculate_route_priority(), 2)
        self.assertEqual(address3.calculate_route_priority(), 3)
        self.assertEqual(address4.calculate_route_priority(), float("inf"))