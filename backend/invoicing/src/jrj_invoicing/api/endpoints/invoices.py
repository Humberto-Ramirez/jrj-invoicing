from typing import Any, List

from fastapi import APIRouter, Depends
from jrj_invoicing import schemas
from jrj_invoicing.api import deps
from jrj_invoicing.persistence import crud
from jrj_invoicing.utils.Reporting import Reporting
from sqlalchemy.orm import Session
from starlette.responses import FileResponse

router = APIRouter()


@router.get("/", response_model=List[schemas.InvoiceEntityOut])
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


@router.post("/add", response_model=schemas.InvoiceEntity)
def create_invoice(
        *,
        db: Session = Depends(deps.get_db),
        invoice: schemas.InvoiceDto
) -> Any:
    """
    Register a new Invoice
    :param db:
    :param invoice:
    :return:
    """
    invoice_db = crud.invoice.create_active(db, obj_in=invoice)
    return invoice_db


@router.get("/download", response_class=FileResponse)
async def create_report(
        *,
        db: Session = Depends(deps.get_db),
        invoice_id: int
) -> Any:
    """
    Download the invoice_id pdf report
    :param db:
    :param invoice_id: Invoice id
    :return: PDF File
    """
    reports = Reporting()
    return FileResponse(await reports.create_invoice_report(invoice_id))
