#!/usr/bin/python3

"""Contains class for creating state"""
from sqlalchemy import MetaData, create_engine, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base


myMetadata = MetaData()
Base = declarative_base(metadata=myMetadata)

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)