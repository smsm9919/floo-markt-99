from flask import Flask
from extensions import db  # Import db here
# ... other imports (avoid importing models yet)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_uri'
db.init_app(app)

# Import models AFTER initializing db
with app.app_context():
    from models import User, Category, Product, PriceNegotiation, Message, ChatMessage

# Now import routes or register blueprints
# ... rest of your app setup