# import sqlalchemy
# from sqlalchemy import column, create_engine, Table, MetaData
# from sqlalchemy.ext.declerative import declerative_base
# from sqlalchemy import (Integer, String, Float, Text)
# from scrapy.utils.project import get_project_settings

# Base=declerative_base()
# def db_connection():
#     return create_engine(get_project_settings().get("CONNECTION_STRING"))

# def create_table(engine):
#     try:
#         Base.metadata.create_all(engine)
#         print("Tables Created")
#     except:
#         print("Error while creating Table")

# class Quote(Base):
#     __tablename__="Quote"

#     id=column(Integer.primary_key=True)
#     Quotes=column('Quotes'.String)
#     Author =Column('Author', String)
#     Tags=Column('Tags',String)

from sqlalchemy import Column, Integer, create_engine, Table, MetaData
# from sqlalchemy.ext.declrative import declrative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy import (Integer, String, Float, Text)
from scrapy.utils.project import get_project_settings


Base = declarative_base()


# def db_connection():
#     return create_engine(
#         get_project_settings().get("CONNECTION_STRING")
#     )

def db_connect():
    return create_engine(
        get_project_settings().get("CONNECTION_STRING")
    )


def create_table(engine):
    try:
        Base.metadata.create_all(engine)
        print("Tables Created")
    except Exception as e:
        print("Error while creating Table")
        print(e)


class Quote(Base):
    __tablename__ = "Quote"

    id = Column(Integer, primary_key=True)
    Quotes = Column('Quotes', String)
    Author = Column('Author', String)
    Tags = Column('Tags', String)
