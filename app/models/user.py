from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(128), nullable=False)
    admin = db.Column(db.Boolean, default=False)

    # Relacionamentos reversos
    messages = db.relationship("Message", backref="autor", lazy=True)
    comments = db.relationship("Comment", backref="autor", lazy=True)

