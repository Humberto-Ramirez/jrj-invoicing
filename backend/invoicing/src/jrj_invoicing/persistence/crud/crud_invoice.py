import datetime
from typing import Union, Dict, Any

from fastapi.encoders import jsonable_encoder
from jrj_invoicing.persistence.crud.base import CRUDBase
from jrj_invoicing.persistence.models import Invoice
from jrj_invoicing.schemas.invoice import InvoiceEntity
from sqlalchemy.orm import Session


class CRUDInvoice(CRUDBase[Invoice, InvoiceEntity, InvoiceEntity]):

    def create_active(self, db: Session, *, obj_in: InvoiceEntity):
        obj_ind_data = jsonable_encoder(obj_in)
        active_obj = db.query(self.model).filter(Invoice.sw_active).first()
        if active_obj:
            new_data = {'sw_active': False, 'report_date': datetime.date.today()}
            upd_item = self.update(db, db_obj=active_obj, obj_in=new_data, )
        db_obj = self.model(**obj_ind_data)  # type: ignore
        db_obj.sw_active = True
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
            self,
            db: Session,
            *,
            db_obj: Invoice,
            obj_in: Union[InvoiceEntity, Dict[str, Any]]
    ) -> InvoiceEntity:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)


invoice = CRUDInvoice(Invoice)
