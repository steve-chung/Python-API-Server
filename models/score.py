from db import db
from sqlalchemy.exc import SQLAlchemyError
from ast import literal_eval

class ScoresModel(db.Model):
  __tablename__ = 'scores'

  id = db.Column(db.Integer, primary_key=True)
  hole_id = db.Column(db.Integer, db.ForeignKey('holes.id'))
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  # stat_id = db.Column(db.Integer, db.ForeignKey('stat.id'))
  game_id = db.Column(db.Integer, db.ForeignKey('games.id'))

  def __init__(self, hole_id, user_id, game_id):
    self.game_id = game_id
    self.hole_id = hole_id
    self.user_id = user_id

  def save_to_db(self):
    try:
      db.session.add(self)
      db.session.commit(self)
      return {'message': 'successfully insert score'}
    except SQLAlchemyError as e:
      print (e)

  @classmethod
  def find_by_id(cls, _id):
    return cls.query.filter_by(id = _id).first() 
