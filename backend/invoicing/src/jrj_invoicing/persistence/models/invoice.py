from jrj_invoicing.persistence.db.base_class import Audit, Base
from sqlalchemy import Column, Integer, Date, Boolean
from sqlalchemy.orm import relationship


class Invoice(Audit, Base):
    id = Column(Integer, primary_key=True, index=True)
    sw_active = Column(Boolean, default=True, nullable=False)
    report_date = Column(Date, nullable=True)
    jobs = relationship("Job", back_populates="invoice")
