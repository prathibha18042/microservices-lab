from sqlalchemy import Column, Integer, Table, MetaData

metadata = MetaData()

orders = Table(
    "orders",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, nullable=False),
    Column("total", Integer, nullable=False),
)
