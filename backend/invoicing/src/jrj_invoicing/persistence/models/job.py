from jrj_invoicing.persistence.db.base_class import Audit, Base
from sqlalchemy import Column, String, Integer, Float, Date, Boolean
from sqlalchemy.orm import relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .material import Order  # noqa: F401


class Job(Audit, Base):
    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, nullable=False)
    materials = relationship("Order", back_populates="job")
