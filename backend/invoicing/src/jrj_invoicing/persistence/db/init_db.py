import logging

from jrj_invoicing import schemas
from jrj_invoicing.persistence import crud
from sqlalchemy.orm import Session

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

materials = [
    {
        "sku": "001",
        "name": "6/12 pitch and Under",
        "description": "6/12 pitch and Under",
        "price": 75
    },
    {
        "sku": "002",
        "name": "7/12 - 8/12 pitch",
        "description": "7/12 - 8/12 pitch",
        "price": 80
    },
    {
        "sku": "003",
        "name": "9/12 - 10/12 pitch",
        "description": "9/12 - 10/12 pitch",
        "price": 85
    },
    {
        "sku": "004",
        "name": "11/12 - 12/12 pitch",
        "description": "11/12 - 12/12 pitch",
        "price": 90
    },
    {
        "sku": "005",
        "name": "13/12 +",
        "description": "13/12 +",
        "price": 0
    },
    {
        "sku": "006",
        "name": "OSB",
        "description": "OSB",
        "price": 20
    },
    {
        "sku": "007",
        "name": "Chimney (Small)",
        "description": "Chimney (Small)",
        "price": 75
    },
    {
        "sku": "008",
        "name": "Chimney (Large)",
        "description": "Chimney (Large)",
        "price": 125
    },
    {
        "sku": "009",
        "name": "Step Flashing @ $3 per foot",
        "description": "Step Flashing @ $3 per foot",
        "price": 3
    },
    {
        "sku": "010",
        "name": "Cricket",
        "description": "Cricket",
        "price": 85
    },
]


def init_db(db: Session) -> None:
    """
    Query the product with key '001'
        If there are no registered product with '001' key, try to save it
    :param db: Current Session
    """
    # Create the tables if not exists
    # base.Base.metadata.create_all(bind=engine)
    product = crud.product.get_by_key(db, key="001")
    if not product:
        product_in = schemas.ProductEntity(
            key="001",
            name="Uno",
            price=float(10.5),
        )
        product_db = crud.product.create_defaults(db, obj_in=product_in)

    for item in materials:
        material_in = schemas.MaterialEntity(**item)
        material = crud.material.get_by_sku(db, sku=material_in.sku)
        if not material:
            material_db = crud.material.create(db, obj_in=material_in)
