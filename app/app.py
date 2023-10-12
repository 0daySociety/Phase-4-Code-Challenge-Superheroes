#!/usr/bin/env python3

from flask import Flask, make_response,jsonify,request
from flask_migrate import Migrate
from flask_restful import Api,Resource
from models import db, Hero,Hero_Power,Power

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)
api=Api(app)



    

class Heroes(Resource):
    def get(self):
        heros = Hero.query.all()

        return jsonify([hero.serialize() for hero in heros])


api.add_resource(Heroes, '/heroes')

class hero_id(Resource):
     def get(self,id):
          hero =Hero.query.get(id)
          response =make_response(jsonify(hero.serialize()),200)
          return response
api.add_resource(hero_id ,"/heroes/<int:id>")  

class power(Resource):
     def get(self):
          _power=Power.query.all()
          power_serialize=[x.serialize()for x in _power]
          response =make_response(jsonify(power_serialize),200)
          return response

api.add_resource(power,"/power")


class power_id(Resource):
     def get(self,id):
          _power =Power.query.get(id)
          if not _power:
               message ={"status":"not found"}
               response =make_response(jsonify(message),404)
               return response
          else:
            response =make_response(jsonify(_power.serialize()),200)
            return response

               
          
     def patch(self, id):
        power = Power.query.get(id)

        if power is None:
            return {'Invalid': 'Power not found'}

        try:
            data = request.get_json()

            if 'description' in data:
                new_description = data['description']
                if not new_description:
                    return jsonify({'errors': ['description must be present']}), 400

                if len(new_description) < 20:
                    return jsonify({'errors': ['description must be at least 20 characters']}), 400

                power.description = new_description
                db.session.commit()
                return jsonify(power.serialize())
            else:
                return {'errors': ['No valid fields for updates']}

        except ValueError as e:
            return jsonify({'errors': [str(e)]}), 400

     
api.add_resource(power_id,"/power/<int:id>")




class hero_powers(Resource):
    def post(self):
        add_power_hero=Hero_Power(
            strength=request.form["strength"],
            hero_id =request.form["hero_id"],
            power_id=request.form["power_id"]
        )
        db.session.add(add_power_hero)
        db.session.commit()
        response =make_response(jsonify(add_power_hero.serialize()),201)
        return response
api.add_resource(hero_powers,"/hero_power")



if __name__ == '__main__':
        
        app.run(port=5555)
