import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_debugtoolbar import DebugToolbarExtension
import config

from checkers import check_env_vars

# instantiate db
db = SQLAlchemy()
migrate = Migrate()
limiter = Limiter(key_func=get_remote_address)
debug_toolbar = DebugToolbarExtension()

def create_app():

    #check_env_vars(['DATABASE_URI', 'SECRET_KEY'])

    app = Flask(__name__)
    

    # Set app configuration
    # if not os.environ.get('FLASK_ENV'):
    #     raise ValueError("env variable doesn't exist")
    if os.environ.get('FLASK_ENV') == 'production':
        app.config.from_object(config.ProductionConfig)
    else:
        app.config.from_object(config.DevelopmentConfig)

    # Jinja template configs
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True
    app.jinja_env.keep_trailing_newline = True

    # add filters
    from filters import embolden, format_hs, format_hslist
    app.jinja_env.filters['embolden'] = embolden
    app.jinja_env.filters['format_hs'] = format_hs
    app.jinja_env.filters['format_hslist'] = format_hslist


    # initialize extensions
    db.init_app(app)    
    migrate.init_app(app, db)
    limiter.init_app(app)
    debug_toolbar.init_app(app)
 
    with app.app_context():
        #TODO: create db/tables and populate if not exists
        #TODO: check for db updates
        #TODO: update if necessary

        # Add Routes
        # Main
        from app.main.routes import main_bp
        app.register_blueprint(main_bp)

        # Canada
        from app.ca.routes import ca_bp
        app.register_blueprint(ca_bp)

    return app
