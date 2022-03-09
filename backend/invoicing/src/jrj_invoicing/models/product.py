from jrj_invoicing.db.base_class import Base
from sqlalchemy import Column, Integer, String, Float, Date, Boolean


class Product(Base):
    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, index=True, unique=True)
    name = Column(String, index=True, nullable=False)
    price = Column(Float)
    creation_date = Column(Date, nullable=False)
    sw_active = Column(Boolean(), default=True)
