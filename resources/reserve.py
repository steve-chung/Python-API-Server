from flask_restful import Resource, reqparse
from flask import jsonify
from flask_jwt_extended import get_jwt_identity,  jwt_required
from models.user import UserModel
from models.games import Game
from models.players import Players
from ast import literal_eval


parser = reqparse.RequestParser()
parser.add_argument(
    'date', help='This field cannot be blank', required=True)
parser.add_argument(
    'course', help='This field cannot be blank', required=True)
parser.add_argument(
    'players', action='append', help='This field cannot be blank', required=True)

class reserveCourse(Resource):
  @jwt_required
  def post(self):
    data = parser.parse_args()
    user_email = get_jwt_identity()
    print(user_email)
    user = UserModel.find_by_email(user_email)
    print(user.id)
    players = data['players']
    
    try:
    
      for player in players:
        convert_player = literal_eval(player)
        print(player)
        print(type(player))
        new_players = Players(
          user_id=user.id,
          email=convert_player['email'],
          name=convert_player['name'],
          aveScore=convert_player['aveScore']
        )
        new_players.save_to_db()
      for player in players:
        convert_player = literal_eval(player)
        new_player = Players.find_by_email(convert_player['email'], user.id)

        new_games = Game(
          course = data['course'],
          date = data['date'],
          user_id = user.id,
          player_id = new_player.id
        )
        new_games.save_to_db()
      
      return {
        'message': 'Course {} was scheduled for {}'.format(data['course'], data['date'])
      }, 200

    except:
      return {'message': 'Something went wrong'}, 500

