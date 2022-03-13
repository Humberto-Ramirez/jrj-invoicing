from typing import Any, List

from fastapi import APIRouter, Depends
from jrj_invoicing import schemas
from jrj_invoicing.api import deps
from jrj_invoicing.persistence import crud
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[schemas.InvoiceEntity])
def read_invoices(
        db: Session = Depends(deps.get_db),
        offset: int = 0,
        limit: int = 100
) -> Any:
    """
    Retrieve invoices
    :param db:
    :param offset:
    :param limit:
    :return:
    """
    invoices = crud.invoice.get_multi(db, skip=offset, limit=limit)
    return invoices
