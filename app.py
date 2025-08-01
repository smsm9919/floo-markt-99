# src/app.py
from flask import Flask
from extensions import db  # Import from extensions

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'your-database-uri'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize db without models
db.init_app(app)

# Import models AFTER db initialization
with app.app_context():
    # Import all models here
    from models import User, Category, Product, PriceNegotiation, Message, ChatMessage
    
    # Create tables (if needed)
    db.create_all()

# Import routes AFTER models
from routes import *  # Assuming you have a routes.py file

if __name__ == '__main__':
    app.run()