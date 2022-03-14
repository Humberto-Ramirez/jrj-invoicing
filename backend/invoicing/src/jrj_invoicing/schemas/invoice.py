import datetime
from typing import Optional, List

from pydantic import BaseModel
from .job import JobEntity


class InvoiceBase(BaseModel):
    id: Optional[int] = None


class InvoiceDto(BaseModel):
    sw_active: Optional[bool] = None
    jobs: List[JobEntity] = []


class InvoiceUpdate(InvoiceDto):
    report_date: Optional[datetime.date] = datetime.date.today()


class InvoiceEntity(InvoiceBase):
    sw_active: Optional[bool] = True

    class Config:
        orm_mode = True


class InvoiceEntityOut(InvoiceEntity):
    report_date: Optional[datetime.date] = None
