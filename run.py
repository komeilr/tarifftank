from app.factory import create_app, db
from app.ca.models import CA2017, CA2018, CA2019

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, CA2017=CA2017, CA2018=CA2018, CA2019=CA2019)