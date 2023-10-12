from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    super_name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime,server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    powers =db.relationship('Power', secondary='hero_powers')

    def serialize(self):
        serial_powers = [power.serialize() for power in self.powers]
        return {
            'id': self.id,
            'name': self.name,
            'super_name': self.super_name,
            'powers': serial_powers
        }

class Power(db.Model, SerializerMixin):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    heroes = db.relationship('Hero', secondary='hero_powers')

    def serialize(self):
        return{
        'id': self.id,
        'name': self.name,
        'description': self.description
    }
    
    @validates('description')
    def validates_description(self, key, description):
        if len(description) < 20:
            raise ValueError('Invalid: Description must be atleast 20 characters')
        return description

class Hero_Power(db.Model, SerializerMixin):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String, nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    hero =  db.relationship('Hero')
    power = db.relationship('Power')

    def serialize(self):
        return self.hero.serialize()
    
    @validates('strength')
    def validate_strength(self, key, strength):
        allowed_strength = ['Strong', 'Weak', 'Average']
        if strength not in allowed_strength:
            raise ValueError(f"{key} must be one of: {', '.join(allowed_strength)}")
        return strength