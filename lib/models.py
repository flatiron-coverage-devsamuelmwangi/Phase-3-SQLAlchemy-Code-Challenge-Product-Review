import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
sys.path.append(os.getcwd)

from sqlalchemy import (create_engine, PrimaryKeyConstraint, Column, String, Integer, ForeignKey)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

engine = create_engine('sqlite:///lib/db/reviews.sqlite', echo=True)
Session = sessionmaker(bind=engine)
session = Session()



class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String())

    def __repr__(self):
        return f'User: {self.name}'

    def reviews(self):
        return session.query(Review).filter_by(user=self).all()

    def products(self):
        reviewed_products = [review.product for review in self.reviews()]
        return list(set(reviewed_products))


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String())
    price = Column(Integer)

    def __repr__(self):
        return f'Product: {self.name}'

    def reviews(self):
        return session.query(Review).filter_by(product=self).all()

    def users(self):
        reviewers = [review.user for review in self.reviews()]
        return list(set(reviewers))

    def leave_review(self, user, star_rating, comment):
        review = Review(product=self, user=user, star_rating=star_rating, comment=comment)
        session.add(review)
        session.commit()

    def print_all_reviews(self):
        for review in self.reviews():
            review.print_review()

    def average_rating(self):
        ratings = [review.star_rating for review in self.reviews()]
        if ratings:
            return sum(ratings) / len(ratings)
        else:
            return 0.0


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    comment = Column(String())
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))

    user = relationship('User', back_populates='reviews')
    product = relationship('Product', back_populates='reviews')

    def user(self):
        return self.user

    def product(self):
        return self.product

    def print_review(self):
        print(f"Review for {self.product.name} by {self.user.name}: {self.star_rating}. {self.comment}")
