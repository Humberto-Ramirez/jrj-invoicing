from typing import Any, List

from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from jrj_invoicing import schemas
from jrj_invoicing.api import deps
from jrj_invoicing.persistence import crud
from sqlalchemy.orm import Session

router = APIRouter()
from loguru import logger


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
    for item in materials:
        json_item = jsonable_encoder(item, exclude=["create_date","sw_active"], exclude_none=True)
        logger.info(json_item)
    return materials
