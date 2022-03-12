from fastapi.encoders import jsonable_encoder
from jrj_invoicing.persistence.crud.base import CRUDBase
from jrj_invoicing.persistence.models.job import Job
from jrj_invoicing.schemas.job import JobEntity
from sqlalchemy.orm import Session


class CRUDJob(CRUDBase[Job, JobEntity, JobEntity]):
    def get_by_invoice(self, db: Session, invoice_id: int):
        return db.query(self.model).filter(self.model.invoice_id == invoice_id).all()

    def create_active(self, db: Session, *, obj_in: JobEntity):
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


job = CRUDJob(Job)
