from app.factory import create_app, db, limiter
from app.ca.models import CA2018, CA2019, CA2020, Section, Chapter

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, CA2018=CA2018, CA2019=CA2019, CA2020=CA2020, Section=Section, Chapter=Chapter, limiter=limiter)