from app.factory import create_app, db
import json

app = create_app()

def execute(query):
    res = None
    with app.app_context():
        res = db.session.execute(query)
    return res.fetchall()

def populate_table(tablename):
    data_path = "app/data/ca"
    json_data = None
    with open(f"{data_path}/{tablename}.json", 'r') as f:
        json_str = f.read()
        json_data = json.loads(json_str)[0]
    return json_data



populate_table('ca2019')
