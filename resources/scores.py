from flask_restful import Resource, reqparse
from flask import jsonify
from flask_jwt_extended import get_jwt_identity,  jwt_required
from models.user import UserModel
from models.games import GameModel
from models.stat import StatModel
from models.score import ScoresModel
from ast import literal_eval


parser = reqparse.RequestParser()
parser.add_argument(
  'game_id', help='This field cannot be blank', required=True
  )
parser.add_argument(
  'hole_id', help='This field cannot be blank', required=True
)
parser.add_argument(
    'firstClub', help='This field cannot be blank', required=True
)
parser.add_argument(
    'firstDistance', help='This field cannot be blank', required=True
)
parser.add_argument(
    'firstClub', help='This field cannot be blank', required=True
)
parser.add_argument(
    'secondClub', help='This field cannot be blank', required=True
)
parser.add_argument(
    'secondDistance', help='This field cannot be blank', required=True
)
parser.add_argument(
    'strokesGreen', help='This field cannot be blank', required=True
)
parser.add_argument(
    'totalShots', help='This field cannot be blank', required=True
)

class Scores(Resource):
  @jwt_required
  def post(self):
    data = parser.parse_args()
    user_email = get_jwt_identity()
    user = UserModel.find_by_email(user_email)
    
    # try:
    #   new_stat = StatModel(
        
    #   )

