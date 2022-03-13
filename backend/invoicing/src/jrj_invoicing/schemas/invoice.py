import datetime
from typing import Optional, List

from pydantic import BaseModel
from .job import JobEntity


class InvoiceBase(BaseModel):
    id: Optional[int] = None


class InvoiceDto(InvoiceBase):
    sw_active: Optional[bool] = None
    jobs: Optional[List[JobEntity]] = []


class InvoiceEntity(InvoiceBase):
    sw_active: Optional[bool] = True
    report_date: Optional[datetime.date] = datetime.date.today()
    jobs: List[JobEntity] = []

    class Config:
        orm_mode = True
