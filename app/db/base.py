import os
from sqlalchemy import (Column,DateTime,Integer,String,Table,create_engine,MetaData)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from databases import Database

DATABASE_URL="postgresql://postgres:reihan1305@localhost:5432/fastapi"

engine = create_engine(DATABASE_URL)
Base = declarative_base()
metadata = MetaData()

blogs = Table(
    "blogs",
    metadata,
    Column("id",Integer,primary_key = True),
    Column("title",String(50)),
    Column("content",String(50))
)

database = Database(DATABASE_URL)