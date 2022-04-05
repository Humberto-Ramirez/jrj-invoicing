from typing import List
from jrj_invoicing.utils.Reporting import Reporting
from jrj_invoicing.persistence.models import Invoice
from jrj_invoicing.schemas.invoice import InvoiceEntityOut
from jrj_invoicing.schemas.job import JobEntity
from jrj_invoicing.persistence import crud
from loguru import logger
from sqlalchemy.orm import Session


async def generate_report(db: Session, invoice_no: int):
    """
    Generate invoice pdf report
    :param db: DB Session
    :param invoice_no: Number of invoice for the report
    :return: Any
    """
    reporting = Reporting()
    invoice = crud.invoice.get(db, invoice_no)
    if invoice:
        logger.info(f"Invoice: {InvoiceEntityOut.from_orm(invoice)}")
    else:
        logger.warning(f"Not exist invoice no {Invoice}")
    # invoices = crud.invoice.get_multi(db, skip=offset, limit=limit)
    return await reporting.create_invoice_report(invoice_no, invoice.jobs)
