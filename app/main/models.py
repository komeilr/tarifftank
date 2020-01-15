from app.factory import db
from datetime import datetime

class ContactMessage(db.Model):
    __tablename__ = "contact_message"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, index=True)
    subject = db.Column(db.String(255), nullable=False)
    message = db.Column(db.Text, nullable=False)    
    date_submitted = db.Column(db.DateTime, nullable=False, default=datetime.now)
    remote_address = db.Column(db.String(255), nullable=False)


    def __repr__(self):
        return f"<ContactMessage {self.subject}>"