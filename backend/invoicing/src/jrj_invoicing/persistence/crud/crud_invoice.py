from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from jrj_invoicing.persistence.crud.base import CRUDBase
from jrj_invoicing.persistence.models import Invoice
from jrj_invoicing.schemas.invoice import InvoiceEntity


class CRUDInvoice(CRUDBase[Invoice, InvoiceEntity, InvoiceEntity]):

    def create_active(self, db: Session, *, obj_in: InvoiceEntity):
        obj_ind_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_ind_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


invoice = CRUDInvoice(Invoice)
