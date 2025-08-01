# src/routes.py
from flask import Blueprint, jsonify
from extensions import db
from models import User, Product  # Safe to import here

main = Blueprint('main', __name__)

@main.route('/')
def home():
    users = User.query.all()
    # ... rest of your route logic