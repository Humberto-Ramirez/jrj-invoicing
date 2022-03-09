import datetime
from typing import Optional

from pydantic import BaseModel


# Shared properties
class ProductBase(BaseModel):
    key: Optional[str] = None
    name: Optional[str] = None
    price: float


# Properties to receive via API on creation
class ProductDto(BaseModel):
    key: str
    ammount: int
    total_ammount: Optional[float] = float(0)


class ProductEntity(ProductBase):
    id: Optional[int] = None
    creation_date: Optional[datetime.date] = None
    sw_active: Optional[bool] = False

    class Config:
        orm_mode = True


class ProductUpdate(ProductBase):
    pass
