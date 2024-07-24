from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    contact_number = db.Column(db.String(20), nullable=False)
    message = db.Column(db.Text, nullable=False)
    def __repr__(self):
        return f'<Contact {self.name}>'