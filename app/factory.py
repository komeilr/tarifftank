import os

from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_debugtoolbar import DebugToolbarExtension
import config

# instantiate db
db = SQLAlchemy()
migrate = Migrate()
limiter = Limiter(key_func=get_remote_address)
debug_toolbar = DebugToolbarExtension()
csrf = CSRFProtect()

def create_app(config_file=None):

    app = Flask(__name__)    

    # Set app configuration
    # if not os.environ.get('FLASK_ENV'):
    #     raise ValueError("env variable doesn't exist")
    if config_file == None:
        if os.environ.get('FLASK_ENV') == 'production':
            app.config.from_object(config.ProductionConfig)
        else:
            app.config.from_object(config.DevelopmentConfig)
    else:
        app.config.from_object(config_file)
    # Jinja template configs
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True
    app.jinja_env.keep_trailing_newline = True

    # add filters
    from filters import embolden, format_hs, format_hslist
    app.jinja_env.filters['embolden'] = embolden
    app.jinja_env.filters['format_hs'] = format_hs
    app.jinja_env.filters['format_hslist'] = format_hslist

    # remove jinja cache limit
    app.jinja_env.cache = {}


    # initialize extensions
    if db:
        db.init_app(app)    
    if migrate: 
        migrate.init_app(app, db)
    if limiter:
        limiter.init_app(app)
    if debug_toolbar:
        debug_toolbar.init_app(app)
    if csrf:
        csrf.init_app(app)
 
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

        # DevBlog
        from app.devblog.routes import devblog_bp
        app.register_blueprint(devblog_bp)

        # Error Handlers
        from app.error_handlers.errorhandlers import error_bp
        app.register_blueprint(error_bp)

    return app
