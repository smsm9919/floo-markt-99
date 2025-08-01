# src/app.py
from flask import Flask
from extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'your-database-uri'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Import models AFTER db initialization
    with app.app_context():
        from . import models  # Import entire models module
        
        # Create tables if needed
        db.create_all()
    
    # Import and register blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run()