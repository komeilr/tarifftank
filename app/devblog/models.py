from datetime import datetime

from app.factory import db

class Blog(db.Model):
    __tablename__ = "dev_blog"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    date_modified = db.Column(db.DateTime, nullable=False, default=datetime.now)


    def __repr__(self):
        return f"<BLOG {self.title}>"
