from Infrastructure.data_base.data_base import SessionLocal, PackageModel, ClientModel

class PackageRepository:
    def __init__(self):
        self.db = SessionLocal()

    def add_package(self, package):
        db_package = PackageModel(
            id=str(package.id),
            client_id=package.client_id,
            delivery_date=package.delivery_date,
            status=package.status,
        )
        self.db.add(db_package)
        self.db.commit()
        self.db.refresh(db_package)
        return db_package

    def get_all_packages(self):
        return self.db.query(PackageModel).join(ClientModel).all()

    def delete_package(self, package_id: str):
        package = self.db.query(PackageModel).filter(PackageModel.id == package_id).first()
        if package:
            self.db.delete(package)
            self.db.commit()

    def get_last_package(self):
        return self.db.query(PackageModel).order_by(PackageModel.id.desc()).first()

    def get_package_by_id(self, package_id: str):
        return self.db.query(PackageModel).filter(PackageModel.id == package_id).first()

    def update_package(self, package):
        db_package = self.db.query(PackageModel).filter(PackageModel.id == package.id).first()

        if db_package:
            db_package.status = package.status
            self.db.commit()
            self.db.refresh(db_package)
            return db_package
        else:
            raise ValueError("Package not found for update")

