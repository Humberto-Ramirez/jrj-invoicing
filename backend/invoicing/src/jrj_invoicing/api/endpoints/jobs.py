from typing import Any, List

from fastapi import APIRouter, Depends
from jrj_invoicing import schemas
from jrj_invoicing.api import deps
from jrj_invoicing.persistence import crud
from loguru import logger
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[schemas.JobEntity])
def read_jobs(
        db: Session = Depends(deps.get_db),
        offset: int = 0,
        limit: int = 100
) -> Any:
    """
    Retrieve Jobs
    :param db:
    :param offset:
    :param limit:
    :return:
    """
    jobs = crud.job.get_multi(db, skip=offset, limit=limit)
    return jobs


@router.post("/add", response_model=List[schemas.JobEntity])
def create_jobs(
        *,
        db: Session = Depends(deps.get_db),
        jobs: List[schemas.JobDto],
) -> Any:
    """
    Register jobs
    :param db:
    :param jobs:
    :return:
    """
    saved_jobs = []
    for item in jobs:
        saved_item = crud.job.create(db, obj_in=item)
        logger.debug(f"Job saved: {schemas.JobEntity.from_orm(saved_item)}")
        saved_jobs.append(saved_item)
    return saved_jobs
