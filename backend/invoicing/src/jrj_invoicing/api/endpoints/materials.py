from typing import Any, List

from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from jrj_invoicing import schemas
from jrj_invoicing.api import deps
from jrj_invoicing.persistence import crud
from loguru import logger
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[schemas.MaterialEntity])
def read_materials(
        db: Session = Depends(deps.get_db),
        offset: int = 0,
        limit: int = 100
) -> Any:
    """
    Retrieve materials
    :param db:
    :param offset:
    :param limit:
    :return:
    """
    materials = crud.material.get_multi(db, skip=offset, limit=limit)
    return materials
