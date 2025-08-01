# src/models.py
from extensions import db  # Changed from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # ... other fields
    # Add relationships if needed

class Category(db.Model):
    # ... your category model

# Add other models (Product, PriceNegotiation, etc.) similarly