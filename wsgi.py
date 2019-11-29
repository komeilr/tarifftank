from app.factory import create_app, db
import config

app = create_app(config.DevelopmentConfig)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db)
