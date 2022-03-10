from typing import Any

from fastapi.encoders import jsonable_encoder
from jrj_invoicing.persistence.crud.base import CRUDBase
from jrj_invoicing.persistence.models import Product
from jrj_invoicing.schemas.product import ProductEntity, ProductUpdate
from sqlalchemy.orm import Session


class CRUDProduct(CRUDBase[Product, ProductEntity, ProductUpdate]):

    def create_defaults(self, db: Session, *, obj_in: ProductEntity) -> Product:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_key(self, db: Session, *, key: Any) -> Product:
        return db.query(self.model).filter(self.model.key == key).first()


product = CRUDProduct(Product)
