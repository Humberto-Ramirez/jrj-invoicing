from typing import Optional

from pydantic import BaseModel

from .material import MaterialEntity


# Shared properties
class OrderBase(BaseModel):
    amount: int


# Properties to receive via API on creation
class OrderDto(OrderBase):
    material_sku: str
    amount: Optional[int] = 0
    total_price: Optional[float] = 0


class OrderEntity(OrderBase):
    total_price: float
    material: MaterialEntity

    class Config:
        orm_mode = True
