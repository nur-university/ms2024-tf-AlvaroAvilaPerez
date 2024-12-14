import unittest
from datetime import datetime
from domain.services.delivery_validation_service import DeliveryValidationService

class TestDeliveryValidationService(unittest.TestCase):

    def test_validate_scheduled_datetime_in_future(self):
        future_datetime = datetime(2024, 12, 25, 12, 0)
        try:
            DeliveryValidationService.validate_scheduled_datetime(future_datetime)
        except ValueError:
            self.fail("validate_scheduled_datetime raised ValueError unexpectedly!")

    def test_validate_scheduled_datetime_in_past(self):
        past_datetime = datetime(2022, 12, 25, 12, 0)
        with self.assertRaises(ValueError):
            DeliveryValidationService.validate_scheduled_datetime(past_datetime)
