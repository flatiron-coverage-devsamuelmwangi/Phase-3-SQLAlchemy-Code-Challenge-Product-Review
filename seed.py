from sqlalchemy.orm import sessionmaker
from lib.models import User, Product, Review
from sqlalchemy import create_engine
import random


engine = create_engine('sqlite:///lib/db/reviews.sqlite')
Session = sessionmaker(bind=engine)
session = Session()

# Create dummy data for testing

# Create users
user1 = User(name="John")
user2 = User(name="Alice")
user3 = User(name="Bob")

# Create products
product1 = Product(name="Product A", price=10)
product2 = Product(name="Product B", price=20)
product3 = Product(name="Product C", price=30)

# Create reviews
review1 = Review(star_rating=4, comment="Great product!", user=user1, product=product1)
review2 = Review(star_rating=5, comment="Excellent!", user=user2, product=product2)
review3 = Review(star_rating=3, comment="Average product.", user=user3, product=product3)

# Add instances to the session
session.add_all([user1, user2, user3, product1, product2, product3, review1, review2, review3])

# Commit the changes to the database
session.commit()
