from urllib import response
from flask import Blueprint, jsonify, request
from car_inventory.helpers import token_required
from car_inventory.models import db,User,Car,car_schema,cars_schema
api=Blueprint('api',__name__,url_prefix = '/api')

@api.route('getdata')
@token_required
def getdata(current_user_token):
    return jsonify({'some':'value',
            'Other':'values'})

@api.route('/cars', methods=['POST'])
@token_required
def create_car(current_user_token):
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    cost_of_production = request.json['cost_of_production']
    make = request.json['make']
    model = request.json['model']
    user_token = current_user_token.token

    car = Car(name,description,price,cost_of_production,make,model,user_token)
    db.session.add(car)
    db.session.commit()

    response = car_schema.dump(car)
    return jsonify(response)

#ALL
@api.route('/cars',methods=['GET'])
@token_required
def get_cars(current_user_token):
    owner = current_user_token.token
    cars = Car.query.filter_by(user_token = owner).all()
    response = cars_schema.dump(cars)
    return jsonify(response)

#ONE
@api.route('/cars/<id>',methods=['GET'])
@token_required
def get_car(current_user_token,id):
    owner = current_user_token.token
    car = Car.query.get(id)
    response = car_schema.dump(car)
    return jsonify(response)