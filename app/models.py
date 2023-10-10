from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'hero'

    id = db.Column(db.Integer, primary_key=True)
    name =db.Column(db.String)
    power_name =db.Column(db.String)
    updated_at=db.Column(db.DateTime(), server_default= db.func.now())
    hero_power = db.relationship("Hero_Power", back_populates="heroes")


class Power(db.Model):
    __tablename__="power"
    id = db.Column(db.Integer,primary_key=True)
    name =db.Column(db.String)
    description =db.Column(db.String)
    updated_at=db.Column(db.DateTime, server_default=db.func.now())
    created_at=db.Column(db.DateTime, server_default=db.func.now())
    power_heros =db.relationship("Hero_Power", back_populates="powers")
    


class Hero_Power(db.Model):
    __tablename__="hero_power"
    id =db.Column(db.Integer,primary_key=True)
    strength =db.Column(db.String)
    hero_id =db.Column(db.Integer, db.ForeignKey("hero.id"))
    power_id =db.Column(db.Integer,db.ForeignKey("power.id"))
    created_at=db.Column(db.DateTime,server_default=db.func.now())
    updated_at =db.Column(db.DateTime, server_default=db.func.now())
    power =db.relationship("Power",back_populates="powerhero")
    hero =db.relationship("Hero",back_populates ="heropower")








# add any models you may need. 