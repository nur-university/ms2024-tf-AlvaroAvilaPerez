from typing import List
from domain.entities.delivery import Delivery


class RouteOptimizationService:
    @staticmethod
    def optimize_routes(deliveries: List[Delivery]):
        return sorted(deliveries, key=lambda d: d.address.calculate_route_priority())
