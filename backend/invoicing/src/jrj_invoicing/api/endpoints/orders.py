from typing import Any, List

from fastapi import APIRouter, Depends
from jrj_invoicing import schemas
from jrj_invoicing.api import deps
from jrj_invoicing.persistence import crud
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
