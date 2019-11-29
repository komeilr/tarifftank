import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    
    if os.environ.get('FLASK_ENV') == 'production':
        app.config.from_object(config.ProductionConfig)
    else:
        app.config.from_object(config.DevelopmentConfig)
        
    db.init_app(app)

    with app.app_context():
        from app.main.routes import main_bp
        app.register_blueprint(main_bp)

    return app
