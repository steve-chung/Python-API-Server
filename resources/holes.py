from flask_restful import Resource, reqparse
from db import db
from flask import jsonify
from flask_jwt_extended import jwt_required, fresh_jwt_required, get_jwt_identity
from models.user import UserModel
from models.games import GameModel
from models.holes import HolesModel
from models.score import ScoresModel
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
    user_email = get_jwt_identity()
    user = UserModel.find_by_email(user_email)
    holes = data['holes']
    game_id = data['game_id']
    try: 
      for hole in holes:
        converted_hole = literal_eval(hole)
        print(converted_hole)
        for _key, _val in converted_hole.items():
          new_holes = HolesModel(
            hole_number = _key,
            par = _val
          )
          new_holes.save_to_db()
          new_score = ScoresModel(game_id = game_id, hole_id = new_holes.id, 
            user_id = user.id, stat_id = None )
          new_holes.hole.append(user)
          db.session.add(new_score)
          db.session.commit()
      return {
        'message': 'Holes info has ben saved'
      }, 200

    except Exception as e:
      print(e)
      return {
        'message': 'Something went wrong'
      }, 500
