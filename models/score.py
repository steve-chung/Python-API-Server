from db import db
from sqlalchemy.exc import SQLAlchemyError
from ast import literal_eval

class Scores(db.Model):
  __tablename__ = 'scores'

  id = db.Column(db.Integer, primary_key=True)
  hole_id = db.relationship('Holes', lazy='dynamic')
  user_id = db.relationship('UserModel', lazy='dynamic')
  stat_id = db.relationship('StatModel', lazy='dynamic')
  game_id = db.relationship('GameModel', lazy='dynamic')

  def __init__(self, hole_id, user_id, stat_id, game_id):
    self.game_id = game_id
    self.hole_id = hole_id
    self.user_id = user_id
    self.game_id = game_id

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
