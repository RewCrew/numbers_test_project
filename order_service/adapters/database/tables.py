from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    Date,
    Float,
    Integer,
    MetaData,
    String,
    Table,
)

naming_convention = {
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s'
}

metadata = MetaData(naming_convention=naming_convention)

orders = Table(
    'orders', metadata,
    Column('id', Integer, nullable= False),
    Column('order_id', Integer, primary_key=True),
    Column('price_us', Integer, nullable=False),
    Column('date', String, nullable=False),
    Column('price_rub', Float, nullable=False),
)

