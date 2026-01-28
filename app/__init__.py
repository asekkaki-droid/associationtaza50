from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

from flask_mail import Mail

db = SQLAlchemy()
mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    mail.init_app(app)

    # Initialize LoginManager (we'll need it for admin)
    from flask_login import LoginManager
    login_manager = LoginManager()
    login_manager.login_view = 'main.login'
    login_manager.init_app(app)
    
    # User loader callback for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User
        return User.query.get(int(user_id))

    from app.routes import main
    app.register_blueprint(main)
    
    # Import models to ensure they are registered with SQLAlchemy
    with app.app_context():
        from app import models
        db.create_all()

    return app
