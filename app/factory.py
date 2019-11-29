import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

# instantiate db
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Set app configuration
    if not os.environ.get('FLASK_ENV'):
        raise ValueError("env variable doesn't exist")
    if os.environ.get('FLASK_ENV') == 'production':
        app.config.from_object(config.ProductionConfig)
    else:
        app.config.from_object(config.DevelopmentConfig)

    # initialize DB
    db.init_app(app)
 
    with app.app_context():
        #TODO: create db/tables and populate if not exists
        #TODO: check for db updates
        #TODO: update if necessary

        # Add Routes
        from app.main.routes import main_bp
        app.register_blueprint(main_bp)

    return app
