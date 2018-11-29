from db import db
from models.games import Game
from sqlalchemy.exc import SQLAlchemyError
from ast import literal_eval

class Scores(db.Model):
  __tablename__ = 'scores'

  id = db.Column(db.Integer, primary_key=True)
  hole_id = db.Column(db.Integer, db.ForeignKey('holes.id'))
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  stat_id = db.Column(db.Integer, db.ForeignKey('stats.id'))
  game_id = db.Column(db.Integer, db.ForeignKey('games.id'))

  def __init__(self, hole_id, user_id, stat_id, game_id):
    self.game_id = game_id
    self.hole_id = hole_id
    self.user_id = user_id
    self.game_id = game_id

    