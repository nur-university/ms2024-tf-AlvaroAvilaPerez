from Infrastructure.data_base.data_base import SessionLocal, PackageModel


class PackageRepository:
    def __init__(self):
        self.db = SessionLocal()

    def add_package(self, package):
        db_package = PackageModel(
            id=str(package.id),
            client_name=package.client_name,
            delivery_date=package.delivery_date,
            address=package.address,
            status=package.status
        )
        self.db.add(db_package)
        self.db.commit()
        self.db.refresh(db_package)
        return db_package

    def get_all_packages(self):
        return self.db.query(PackageModel).all()

    def delete_package(self, package_id: str):
        package = self.db.query(PackageModel).filter(PackageModel.id == package_id).first()
        if package:
            self.db.delete(package)
            self.db.commit()

    def get_last_package(self):
        return self.db.query(PackageModel).order_by(PackageModel.id.desc()).first()
