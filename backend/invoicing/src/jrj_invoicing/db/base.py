# Import all the models, so that Base has them before being
# imported by Alembic
from jrj_invoicing.db.base_class import Base
from jrj_invoicing.models.product import Product
