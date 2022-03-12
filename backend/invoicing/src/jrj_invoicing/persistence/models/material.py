from jrj_invoicing.persistence.db.base_class import Audit, Base
from sqlalchemy import Column, Integer, String, Float, Date, Boolean


class Material(Base, Audit):
    sku = Column(String, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float)
    sw_active = Column(Boolean, default=True)
