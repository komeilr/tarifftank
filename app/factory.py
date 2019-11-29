from flask import Flask

def create_app(configObject):
    app = Flask(__name__)
    app.config.from_object(configObject)

    with app.app_context():
        from app.main.routes import main_bp
        app.register_blueprint(main_bp)

    return app
