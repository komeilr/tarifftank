from flask import Flask

def create_app():
    app = Flask(__name__)

    with app.app_context():
        from app.main.routes import main_bp
        app.register_blueprint(main_bp)

    return app
