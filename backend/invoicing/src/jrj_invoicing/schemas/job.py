from typing import Optional

from pydantic import BaseModel


class JobBase(BaseModel):
    id: Optional[int] = None


class JobDto(JobBase):
    address: str
    invoice_id: int


class JodEntity(JobDto):
    class Config:
        orm_mode = True
