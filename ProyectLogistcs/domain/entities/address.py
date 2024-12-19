class Address:

    def __init__(self, street: str, city: str, zone: str):

        self.street = street
        self.city = city
        self.zone = zone

    def calculate_route_priority(self) -> int:
        zone_priority_map = {
            "central": 1,
            "north": 2,
            "south": 3
        }
        return zone_priority_map.get(self.zone.lower(), float("inf"))