from typing import Optional

from pydantic import BaseModel


# Shared properties
class MaterialBase(BaseModel):
    sku: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    price: float


# Material In properties
class MaterialEntity(MaterialBase):
    sw_active: Optional[bool] = False

    class Config:
        orm_mode = True
