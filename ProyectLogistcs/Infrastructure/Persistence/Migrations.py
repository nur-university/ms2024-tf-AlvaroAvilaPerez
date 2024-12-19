from sqlalchemy import create_engine
from Infrastructure.data_base.data_base import Base, DATABASE_URL

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)