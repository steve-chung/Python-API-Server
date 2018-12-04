from flask_restful import Resource, reqparse
from flask import jsonify
from flask_jwt_extended import jwt_required, fresh_jwt_required
from models.user import UserModel
from models.games import GameModel
from models.holes import HolesModel
from ast import literal_eval


parser = reqparse.RequestParser()
parser.add_argument(
    'game_id', help='This field cannot be blank', required=True)
parser.add_argument(
    'holes', action='append', help='This field cannot be blank', required=True)


class createHoles(Resource):
  @fresh_jwt_required
  def post(self):
    data = parser.parse_args()
    holes = data['holes']
    game_id = data['game_id']
    try: 
      for hole in holes:
        converted_hole = literal_eval(hole)
        print(converted_hole)
        for _key, _val in converted_hole.items():
          new_holes = HolesModel(
            game_id = game_id,
            hole_number = _key,
            par = _val
          )
          new_holes.save_to_db()
      return {
        'message': 'Holes info has ben saved'
      }, 200

    except:
      return {
        'message': 'Something went wrong'
      }, 500