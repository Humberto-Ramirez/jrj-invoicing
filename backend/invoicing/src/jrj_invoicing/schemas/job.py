from typing import Optional, List

from jrj_invoicing.schemas.order import OrderEntity
from pydantic import BaseModel


class JobBase(BaseModel):
    id: Optional[int] = None


class JobDto(BaseModel):
    address: str
    invoice_id: int


class JobEntity(JobDto, JobBase):
    orders: List[OrderEntity] = []

    class Config:
        orm_mode = True
