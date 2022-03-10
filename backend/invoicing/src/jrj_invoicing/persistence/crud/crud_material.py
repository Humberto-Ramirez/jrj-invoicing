from typing import Any

from jrj_invoicing.persistence.crud.base import CRUDBase
from jrj_invoicing.persistence.models import Material
from jrj_invoicing.schemas.material import MaterialEntity
from sqlalchemy.orm import Session


class CRUDMaterial(CRUDBase[Material, MaterialEntity, MaterialEntity]):

    def get_by_sku(self, db: Session, *, sku: Any) -> Material:
        return db.query(self.model).filter(self.model.sku == sku).first()


material = CRUDMaterial(Material)
