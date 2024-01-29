from datetime import datetime
import os

import sqlalchemy
from sqlalchemy import (Column, ForeignKey, Integer, MetaData, String, Table, UniqueConstraint,
                        create_engine, literal_column)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import Date, DateTime, Float

ALL_COLUMNS = literal_column('*')


def get_db_url() -> str:
    return 'postgresql://%s:%s@%s:%s/%s' % (
        os.getenv('POSTGRES_USER', 'hamza'),
        os.getenv('POSTGRES_PASSWORD', 'hamza_password'),
        os.getenv('POSTGRES_HOST', 'ec2-54-204-226-44.compute-1.amazonaws.com'),
        os.getenv('POSTGRES_PORT', '5432'),
        os.getenv('POSTGRES_DB', 'users'),
    )


database_url = get_db_url()
engine = create_engine(database_url)
metadata = MetaData(bind=engine)

new_uuid = sqlalchemy.text("uuid_generate_v4()")
now = datetime.utcnow
default_now = dict(
    default=now,
    server_default=sqlalchemy.func.now()
)

users = Table("users", metadata,
              Column('user_id', UUID(as_uuid=True), primary_key=True, server_default=new_uuid),
              Column('name', String, nullable=False),
              Column('date_of_birth', Date),
              Column('email', String, nullable=False),
              Column('height', Float),
              Column("weight", Float),
              Column('address_id', None, ForeignKey('addresses.address_id')),
              Column('created_at', DateTime, nullable=False, **default_now),
              Column('updated_at', DateTime, nullable=False, onupdate=now, **default_now),
              Column("favourite_color", Integer, nullable=True),
              UniqueConstraint("name", "email"),
              )

addresses = Table("addresses", metadata,
                  Column('address_id', UUID(as_uuid=True), primary_key=True,
                         server_default=new_uuid),
                  Column('zip_code', String, nullable=False),
                  Column('state', Integer, nullable=False),
                  Column('street', String),
                  Column('house_num', Integer),
                  Column('created_at', DateTime, nullable=False, **default_now),
                  Column('updated_at', DateTime, nullable=False, onupdate=now, **default_now),
                  UniqueConstraint("zip_code", "state", "house_num")
                  )
