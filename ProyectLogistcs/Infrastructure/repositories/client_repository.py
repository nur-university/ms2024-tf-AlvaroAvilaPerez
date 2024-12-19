from Infrastructure.data_base.data_base import ClientModel, SessionLocal


class ClientRepository:
    def __init__(self):
        self.db = SessionLocal()

    def add_client(self, client):
        db_client = ClientModel(
            id=str(client.id),
            first_name=client.first_name,
            last_name=client.last_name,
            address=client.address,
            plan=client.plan,
            age=client.age,
            size=client.size,
            weight=client.weight
        )
        self.db.add(db_client)
        self.db.commit()
        self.db.refresh(db_client)
        return db_client

    def get_all_clients(self):
        return self.db.query(ClientModel).all()

    def delete_client(self, client_id: str):
        client = self.db.query(ClientModel).filter(ClientModel.id == client_id).first()
        if client:
            self.db.delete(client)
            self.db.commit()

    def get_client_by_id(self, client_id: str):
        return self.db.query(ClientModel).filter(ClientModel.id == client_id).first()
