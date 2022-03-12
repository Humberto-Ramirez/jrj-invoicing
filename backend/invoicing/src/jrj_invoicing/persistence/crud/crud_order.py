from fastapi.encoders import jsonable_encoder
from jrj_invoicing.persistence.crud.base import CRUDBase
from jrj_invoicing.persistence.models import Order
from jrj_invoicing.schemas.order import OrderEntity
from sqlalchemy.orm import Session


class CRUDOrder(CRUDBase[Order, OrderEntity, OrderEntity]):
    def get_by_job_sku(self, db: Session, *, job: int, sku: str):
        result = db.query(self.model).filter(self.model.job_id == job and self.model.material_sku == sku).all()
        return result

    def create_job_order(self, db: Session, *, obj_in: OrderEntity, job: int):
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, job_id=job)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


order = CRUDOrder(Order)
