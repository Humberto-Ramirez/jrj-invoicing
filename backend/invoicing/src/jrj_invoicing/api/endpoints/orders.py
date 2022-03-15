from typing import Any, List

from fastapi import APIRouter, Depends
from jrj_invoicing import schemas
from jrj_invoicing.api import deps
from jrj_invoicing.persistence import crud
from loguru import logger
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[schemas.OrderEntity])
def read_orders(
        db: Session = Depends(deps.get_db),
        offset: int = 0,
        limit: int = 100
) -> Any:
    """
    Retrieve orders
    :param db:
    :param offset:
    :param limit:
    :return:
    """
    orders = crud.order.get_multi(db, skip=offset, limit=limit)
    return orders


@router.post("/{job_id}", response_model=List[schemas.OrderEntity])
def create_orders(
        db: Session = Depends(deps.get_db),
        *,
        job_id: int,
        orders: List[schemas.OrderDto],
) -> Any:
    """
    Create orders
    :param job_id:
    :param db:
    :param orders:
    :return:
    """
    saved_orders = crud.order.create_orders(db, objs_in=orders, job=job_id)
    for item in saved_orders:
        logger.info(f"Saved order: {schemas.OrderEntity.from_orm(item)}")
    return saved_orders
