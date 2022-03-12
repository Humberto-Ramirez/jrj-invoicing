from jrj_invoicing.persistence.db.base_class import Audit, Base
from sqlalchemy import Column, String, Float, Boolean, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Material(Base, Audit):
    sku = Column(String, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float)
    sw_active = Column(Boolean, default=True)
    order = relationship("Order", back_populates="material")


class Order(Base, Audit):
    id = Column(String, primary_key=True, index=True)
    material_sku = Column(String, ForeignKey("material.sku"))
    amount = Column(Integer, nullable=False, default=0)
    total_price = Column(Float, nullable=False, default=0)
    material = relationship("Material", back_populates="order")
