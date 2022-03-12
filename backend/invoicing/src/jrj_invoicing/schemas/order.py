#     id = Column(String, primary_key=True, index=True)
#     amount = Column(Integer, nullable=False, default=0)
#     total_price = Column(Float, nullable=False, default=0)
#     material = relationship("Material", back_populates="order")
#     material_sku = Column(String, ForeignKey("material.sku"))
#     job = relationship("Job", back_populates="materials")
#     job_id = Column(Integer, ForeignKey("job.id"))

from typing import Optional

from pydantic import BaseModel


# Shared properties
class OrderBase(BaseModel):
    material_sku: str
    amount: int


# Properties to receive via API on creation
class OrderDto(OrderBase):
    material_sku: str
    amount: Optional[int] = 0
    total_price: Optional[float] = 0


class OrderEntity(OrderBase):
    total_price: float
    job_id: int

    class Config:
        orm_mode = True
