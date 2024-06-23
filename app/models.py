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
    quests = db.relationship('Quest', backref='assignee', lazy=True)
    skills = db.relationship('Skill', backref='owner', lazy=True)  # Přidáno

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200))
    item_type = db.Column(db.String(50), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)

class Enemy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    hp = db.Column(db.Integer, nullable=False)
    strength = db.Column(db.Integer, nullable=False)

class Quest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200))
    is_completed = db.Column(db.Boolean, default=False)
    reward = db.Column(db.String(200), nullable=False)  # Přidáno
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)


class Skill(db.Model):  # Přidáno
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200))
    skill_type = db.Column(db.String(50), nullable=False)
    power = db.Column(db.Integer, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)

class ShopItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200))
    item_type = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
