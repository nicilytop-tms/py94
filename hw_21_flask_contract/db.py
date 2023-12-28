from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql.schema import Column
from sqlalchemy import types


engine = create_engine(
    "postgresql+psycopg2://prod_user:prod_user_password@localhost/product_system"
)


class Base(DeclarativeBase):
    ...


class Product(Base):
    __tablename__ = "products"
    id = Column("id", types.Integer(), primary_key=True)
    name = Column("name", types.String(), nullable=False)
    proteins = Column("proteins", types.Float(), nullable=True)
    fats = Column("fats", types.Float(), nullable=True)
    carbs = Column("carbs", types.Float(), nullable=True)
    grs = Column("grs", types.Float(), nullable=False)


Base.metadata.create_all(engine)
