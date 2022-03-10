import datetime
import logging

from jrj_invoicing import schemas
from jrj_invoicing.persistence import crud
from jrj_invoicing.persistence.db import base
from jrj_invoicing.persistence.db.session import engine
from sqlalchemy.orm import Session

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init_db(db: Session) -> None:
    """
    Query the product with key '001'
        If there are no registered product with '001' key, try to save it
    :param db: Current Session
    """
    # Create the tables if not exists
    base.Base.metadata.create_all(bind=engine)
    product = crud.product.get_by_key(db, key="001")
    if not product:
        product_in = schemas.ProductEntity(
            key="001",
            name="Uno",
            price=float(10.5),
            creation_date=datetime.date(year=2021, month=1, day=1)
        )
        product_db = crud.product.create_defaults(db, obj_in=product_in)
