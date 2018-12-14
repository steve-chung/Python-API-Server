from flask_restful import Resource, reqparse
from db import db
from flask import jsonify
from flask_jwt_extended import jwt_required, fresh_jwt_required, get_jwt_identity
from models.user import UserModel
from models.games import GameModel
from models.holes import HolesModel
from models.score import ScoresModel
from models.stat import StatModel
from ast import literal_eval


parser = reqparse.RequestParser()
parser.add_argument(
    'game_id', help='This field cannot be blank', required=True)
parser.add_argument(
    'hole_id', help='This field cannot be blank', required=True)
parser.add_argument(
    'firstClub', help='This field cannot be blank', required=True)
parser.add_argument(
    'firstDistance', help='This field cannot be blank', required=True)
parser.add_argument(
    'secondClub', help='This field cannot be blank', required=True)
parser.add_argument(
    'secondDistance', help='This field cannot be blank', required=True)
parser.add_argument(
    'stroksGreen', help='This field cannot be blank', required=True)
parser.add_argument(
    'totalShot', help='This field cannot be blank', required=True)

class Stat(Resource):
  @fresh_jwt_required
  def post(self):
    data = parser.parse_args()
    user_email = get_jwt_identity()
    user = UserModel.find_by_email(user_email)
    hole_id = data['hole_id']
    game_id = data['game_id']
    firstClub = data['firstClub']
    firstDistance = data['firstDistance']
    secondClub = data['secondClub']
    secondDistance = data['secondDistance']
    stroksGreen = data['stroksGreen']
    totalShot = data['totalShot']
    try:
      new_stat = StatModel(firstClub = firstClub, firstDistance = firstDistance,
        secondClub = secondClub, secondDistance = secondDistance, stroksGreen = stroksGreen,
        totalShot = totalShot)
      new_stat.save_to_db()
      ScoresModel.update_stat_id(user_id=user.id, game_id=game_id, hole_id=hole_id, stat_id = new_stat.id)
      return {'message': 'successfully add hole {}'.format(hole_id)}
    except Exception as e:
      print(e)
      return {'message': 'something went wrong'}
