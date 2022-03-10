# Import all the models, so that Base has them before being
# imported by Alembic
from jrj_invoicing.persistence.db.base_class import Audit, Base
from jrj_invoicing.persistence.models.product import Product
