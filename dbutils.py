from app.factory import create_app, db

app = create_app()

with app.app_context():
    res = db.session.execute('describe test;')
    print(res.fetchall())