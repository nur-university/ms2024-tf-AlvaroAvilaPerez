from sqlalchemy.orm import aliased, joinedload

from Infrastructure.data_base.data_base import SessionLocal, PackageModel, ClientModel, DeliveryModel, \
    DeliveryPersonModel


class DeliveryRepository:
    def __init__(self):
        self.db = SessionLocal()

    def add_delivery(self, delivery):
        db_delivery = DeliveryModel(
            id=str(delivery.id),
            package_id=delivery.package_id,
            delivery_person_id=delivery.delivery_person_id,
        )
        self.db.add(db_delivery)
        self.db.commit()
        self.db.refresh(db_delivery)
        return db_delivery

    def get_all_delivery(self):
        client_alias = aliased(ClientModel)

        deliveries = (
            self.db.query(DeliveryModel)
            .join(PackageModel, DeliveryModel.package_id == PackageModel.id)
            .join(client_alias, client_alias.id == PackageModel.client_id)
            .join(DeliveryPersonModel, DeliveryPersonModel.id == DeliveryModel.delivery_person_id)
            .options(
                joinedload(DeliveryModel.package).joinedload(PackageModel.client),
                joinedload(DeliveryModel.delivery_person)
            )
            .all()
        )
        return deliveries

    def delete_delivery(self, delivery_id: str):
        delivery = self.db.query(DeliveryModel).filter(DeliveryModel.id == delivery_id).first()
        if delivery:
            self.db.delete(delivery)
            self.db.commit()

    def get_delivery_by_id(self, delivery_id: str):
        return self.db.query(DeliveryModel).filter(DeliveryModel.id == delivery_id).first()


