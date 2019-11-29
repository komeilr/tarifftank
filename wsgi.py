from app.factory import create_app
import config

app = create_app(config.DevelopmentConfig)
