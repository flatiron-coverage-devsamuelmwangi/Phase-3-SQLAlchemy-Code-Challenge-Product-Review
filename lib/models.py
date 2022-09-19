import os
import sys

sys.path.append(os.getcwd)

from sqlalchemy import (create_engine, PrimaryKeyConstraint, Column, String, Integer)

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

engine = create_engine('sqlite:///db/reviews.db', echo=True)

# class Review(Base):
#     pass


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String())


    def __repr__(self):
        return f'User: {self.name}'


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String())
    price = Column(Integer)


    def __repr__(self):
        return f'Product: {self.name}'
