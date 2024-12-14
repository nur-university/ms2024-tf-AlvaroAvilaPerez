from Infrastructure.data_base.data_base import DeliveryModel, SessionLocal
from domain.entities.delivery import Delivery


class DeliveryRepository:
    def __init__(self):
        self.db = SessionLocal()

    def add_delivery(self, delivery: Delivery):
        """
        Crea un nuevo delivery en la base de datos.
        """
        db_delivery = DeliveryModel(
            id=str(delivery.id),
            person_id=str(delivery.person_id),
            package_id=str(delivery.package_id),
            client_name=delivery.client_name,
            delivery_date=delivery.delivery_date,
            address=delivery.address,
            status=delivery.status
        )
        self.db.add(db_delivery)
        self.db.commit()
        self.db.refresh(db_delivery)
        return db_delivery

    def get_all_deliveries(self):
        """
        Obtiene todos los deliveries registrados en la base de datos.
        """
        return self.db.query(DeliveryModel).all()

    def delete_delivery(self, delivery_id: str):
        """
        Elimina un delivery de la base de datos.
        """
        delivery = self.db.query(DeliveryModel).filter(DeliveryModel.id == delivery_id).first()
        if delivery:
            self.db.delete(delivery)
            self.db.commit()