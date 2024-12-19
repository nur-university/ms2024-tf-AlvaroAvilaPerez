from sqlalchemy import create_engine, Column, String, Enum, Date, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from domain.enums.delivery_person_status import DeliveryPersonStatus
from domain.enums.package_status import PackageStatus
from domain.enums.plan import Plan
from domain.enums.zone import Zone

Base = declarative_base()


class DeliveryPersonModel(Base):
    __tablename__ = 'delivery_persons'

    id = Column(String, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    zone = Column(Enum(Zone))
    status = Column(Enum(DeliveryPersonStatus))

    deliveries = relationship('DeliveryModel', back_populates='delivery_person')

class DeliveryModel(Base):
    __tablename__ = "deliveries"

    id = Column(String, primary_key=True)
    package_id = Column(String, ForeignKey('packages.id'), nullable=False)
    delivery_person_id = Column(String, ForeignKey('delivery_persons.id'), nullable=False)

    package = relationship('PackageModel', back_populates='deliveries')
    delivery_person = relationship('DeliveryPersonModel', back_populates='deliveries')

class PackageModel(Base):
    __tablename__ = 'packages'

    id = Column(String, primary_key=True)
    client_id = Column(String, ForeignKey('clients.id'), nullable=False)
    delivery_date = Column(Date)
    status = Column(Enum(PackageStatus), default=PackageStatus.pending)

    client = relationship('ClientModel', back_populates='packages')
    deliveries = relationship('DeliveryModel', back_populates='package')

class ClientModel(Base):
    __tablename__ = 'clients'

    id = Column(String, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    address = Column(String)
    plan = Column(Enum(Plan))
    age = Column(Integer)
    size = Column(String)
    weight = Column(String)

    # Relaciones
    packages = relationship('PackageModel', back_populates='client')

DATABASE_URL = "sqlite:///logisticstest2.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
