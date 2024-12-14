from sqlalchemy import create_engine, Column, String, Enum, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from domain.enums.delivery_person_status import DeliveryPersonStatus
from domain.enums.package_status import PackageStatus
from domain.enums.zone import Zone

Base = declarative_base()


class DeliveryPersonModel(Base):
    __tablename__ = 'delivery_person'

    id = Column(String, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    zone = Column(Enum(Zone))
    status = Column(Enum(DeliveryPersonStatus))

class PackageModel(Base):
    __tablename__ = 'packages'

    id = Column(String, primary_key=True)
    client_name = Column(String)
    delivery_date = Column(Date)
    address = Column(String)
    status = Column(Enum(PackageStatus))

class DeliveryModel(Base):
    __tablename__ = "delivery"

    id = Column(String, primary_key=True)
    person_id = Column(String, index=True)  # Related to DeliveryPerson
    package_id = Column(String, index=True)  # Related to Package
    client_name = Column(String)
    delivery_date = Column(Date)
    address = Column(String)
    status = Column(Enum(PackageStatus), default=PackageStatus.PENDING)


DATABASE_URL = "sqlite:///logistics.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine)