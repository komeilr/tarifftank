from app.factory import create_app, db
from app.ca.models import Section, Chapter
from converters import json_to_obj, json_to_str
import csv


app = create_app()

def execute(query, fetch='all'):
    """ executes query with app context"""
    res = None
    with app.app_context():
        res = db.session.execute(query)
    if fetch == 'one':
        return res.fetchone()
    return res.fetchall()


def pop_table(table):
    """ Populates Tables given table class """
    with app.app_context():
        data = json_to_obj(json_to_str(table.__tablename__))
        for row in data:
            entry = table(**row)
            db.session.add(entry)

        db.session.commit()


def populate_section_notes():

    with app.app_context():
        with open(f'app/data/ca/section-notes-2019.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',', quotechar='"')

            for id, number, title, notes, sub, sup, stat in reader:
                if number == 'Number':
                    continue
                entry = Section(id=id, number=number, title=title, notes=notes, 
                                subheading_notes=sub, supplementary_notes=sup,
                                statistical_notes=stat)
                db.session.add(entry)

            db.session.commit()
            

def populate_chapter_notes():

    with app.app_context():
        with open(f'app/data/ca/chapter-notes-2019.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',', quotechar='"')

            for chapter, title, notes, sub, sup, stat, section in reader:
                if title == 'TITLE':
                    continue
                entry = Chapter(chapter=chapter, title=title, notes=notes, 
                                subheading_notes=sub, supplementary_notes=sup,
                                statistical_notes=stat, section_id=section)
                db.session.add(entry)

            db.session.commit()



populate_chapter_notes()
