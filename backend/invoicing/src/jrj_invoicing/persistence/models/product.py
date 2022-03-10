from jrj_invoicing.persistence.db.base_class import Base, Audit
from sqlalchemy import Column, Integer, String, Float, Boolean


class Product(Audit, Base):
    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, index=True, unique=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float)
    sw_active = Column(Boolean(), default=True)
