from app import db

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    character_class = db.Column(db.String(80), nullable=False)
    strength = db.Column(db.Integer, default=10)
    intelligence = db.Column(db.Integer, default=10)
    dexterity = db.Column(db.Integer, default=10)
    level = db.Column(db.Integer, default=1)
    experience = db.Column(db.Integer, default=0)
    inventory = db.relationship('Item', backref='owner', lazy=True)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200))
    owner_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
