import os
import csv
import json

from app.factory import create_app, db, limiter
from app.ca.models import CA2018, CA2019, CA2020, Section, Chapter
import click


app = create_app()

@app.cli.command(name='buildapp')
def create():
    """Builds database"""    
     
    try:
        if "migrations" not in os.listdir():
            print("Initializing database")
            os.system("flask db init")
        print('Migrating database')
        os.system("flask db migrate")

        print('Upgrading database')
        os.system("flask db upgrade")


    except Exception as e:
        print(e)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, CA2018=CA2018, CA2019=CA2019, CA2020=CA2020, Section=Section, Chapter=Chapter, limiter=limiter)