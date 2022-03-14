from typing import TYPE_CHECKING

from jrj_invoicing.persistence.db.base_class import Audit, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from .material import Order  # noqa: F401


class Job(Audit, Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    address = Column(String, nullable=False)
    orders = relationship("Order", back_populates="job")
    invoice = relationship("Invoice", back_populates="jobs")
    invoice_id = Column(Integer, ForeignKey("invoice.id"))
