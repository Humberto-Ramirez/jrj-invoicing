from typing import TYPE_CHECKING

from jrj_invoicing.persistence.db.base_class import Audit, Base
from sqlalchemy import Column, String, Float, Boolean, ForeignKey, Integer
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from .job import Job  # noqa: F401


class Material(Base, Audit):
    sku = Column(String, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float)
    sw_active = Column(Boolean, default=True)
    order = relationship("Order", back_populates="material")


class Order(Base, Audit):
    amount = Column(Integer, nullable=False, default=0)
    total_price = Column(Float, nullable=False, default=0)
    material = relationship("Material", back_populates="order")
    material_sku = Column(String, ForeignKey("material.sku"), primary_key=True)
    job = relationship("Job", back_populates="materials")
    job_id = Column(Integer, ForeignKey("job.id"), primary_key=True)
