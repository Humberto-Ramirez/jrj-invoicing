from fastapi import APIRouter

from .endpoints import materials, orders, invoices

api_router = APIRouter()

api_router.include_router(materials.router, prefix="/materials", tags=["materials"])
api_router.include_router(orders.router, prefix="/orders", tags=["orders"])
api_router.include_router(invoices.router, prefix="/invoices", tags=["invoices"])
