# src/routes.py
from app import app
from extensions import db
from models import User, Product  # Import models here

# Define all your routes and view functions
@app.route('/')
def home():
    # ... implementation