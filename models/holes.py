from db import db
from sqlalchemy.exc import SQLAlchemyError
from ast import literal_eval

class HolesModel(db.Model):
  __tablename__ = 'holes'

  id = db.Column(db.Integer, primary_key=True)
  game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
  game = db.relationship('GameModel')
  hole_number = db.Column(db.Integer, nullable=False)
  par = db.Column(db.Integer, nullable=False)


  def __init__(self, game_id, hole_number, par):
    self.game_id = game_id
    self.hole_number = hole_number
    self.par = par

  def save_to_db(self):
    try:
      db.session.add(self)
      db.session.commit()
      return {'message': 'successfully insert a hole'}
    except SQLAlchemyError as e:
      print(e)