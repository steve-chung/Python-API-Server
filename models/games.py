from db import db
from models.players import Players
from sqlalchemy.exc import SQLAlchemyError
from ast import literal_eval


class Game(db.Model):
  __tablename__ = 'games'

  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  date = db.Column(db.Date)
  player_id = db.Column(db.Integer, db.ForeignKey('players.id'))
  course = db.Column(db.String(30), nullable=False)


  def __init__(self, user_id, course, date, player_id):
    self.user_id = user_id
    self.course = course
    self.player_id = player_id
    self.date = date

  def save_to_db(self):
    try:
      db.session.add(self)
      db.session.commit()
      return {'message': 'successfully insert players'}
    except SQLAlchemyError as e:
      print(e)

  @classmethod
  def find_by_id(cls, _id):
    return cls.query.filter_by(id = _id).first()

  @classmethod
  def find_by_latest(cls, user_id):
    date = cls.date
    return cls.query.filter_by(user_id = user_id).\
           order_by(date.desc()).first()
