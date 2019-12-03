from app.factory import create_app, db
from app.ca.models import CA2017, CA2018, CA2019
from converters import json_to_obj, json_to_str


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


# pop_table(CA2017)
