from typing import List, Optional

from fastapi.encoders import jsonable_encoder
from jrj_invoicing.persistence.crud.base import CRUDBase
from jrj_invoicing.persistence.models import Order
from jrj_invoicing.schemas.order import OrderEntity
from sqlalchemy.orm import Session


class CRUDOrder(CRUDBase[Order, OrderEntity, OrderEntity]):
    def get_by_job_sku(self, db: Session, *, job: int, sku: str) -> Optional[Order]:
        result = db.query(self.model).filter(self.model.material_sku == sku, self.model.job_id == job).first()

        return result

    def create_job_order(self, db: Session, *, obj_in: OrderEntity, job: int) -> Order:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, job_id=job)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def create_orders(self, db: Session, *, objs_in: List[OrderEntity], job: int) -> List[Order]:
        objs_db = []
        for item in objs_in:
            saved_item = self.create_job_order(db, obj_in=item, job=job)
            objs_db.append(saved_item)
        return objs_db


order = CRUDOrder(Order)
