class Address:
    def __init__(self, street: str, city: str, zone: str):
        """
        Representa una dirección con una calle, ciudad y zona.
        :param street: Calle de la dirección.
        :param city: Ciudad de la dirección.
        :param zone: Zona de la dirección.
        """
        self.street = street
        self.city = city
        self.zone = zone

    def calculate_route_priority(self) -> int:
        """
        Calcula la prioridad de la ruta basada en la zona.
        :return: Un entero representando la prioridad.
        """
        zone_priority_map = {
            "central": 1,
            "north": 2,
            "south": 3
        }
        return zone_priority_map.get(self.zone.lower(), float("inf"))