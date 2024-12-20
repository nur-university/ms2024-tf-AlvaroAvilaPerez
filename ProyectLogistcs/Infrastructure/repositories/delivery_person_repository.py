from sqlalchemy.orm import joinedload

from Infrastructure.data_base.data_base import SessionLocal, DeliveryPersonModel, DeliveryModel, PackageModel


class DeliveryPersonRepository:
    def __init__(self):
        self.db = SessionLocal()

    def add_delivery_person(self, delivery_person):
        db_person = DeliveryPersonModel(
            id=str(delivery_person.id),
            first_name=delivery_person.first_name,
            last_name=delivery_person.last_name,
            zone=delivery_person.zone,
            status=delivery_person.status  # Default status already set
        )
        self.db.add(db_person)
        self.db.commit()
        self.db.refresh(db_person)
        return db_person

    def get_all_delivery_persons(self):
        return self.db.query(DeliveryPersonModel).all()

    def delete_delivery_person(self, person_id: str):
        person = self.db.query(DeliveryPersonModel).filter(DeliveryPersonModel.id == person_id).first()
        if person:
            self.db.delete(person)
            self.db.commit()

    def get_delivery_person_by_id(self, delivery_person_id: str):
        return self.db.query(DeliveryPersonModel).filter(DeliveryPersonModel.id == delivery_person_id).first()


