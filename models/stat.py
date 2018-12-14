from db import db
from sqlalchemy.exc import SQLAlchemyError

class StatModel(db.Model):
  __tablename__= 'stat'

  id = db.Column(db.Integer, primary_key=True)
  firstClub = db.Column(db.String(15), nullable = False)
  firstDistance = db.Column(db.Integer, nullable = False)
  secondClub = db.Column(db.String(15), nullable = False)
  secondDistance = db.Column(db.Integer, nullable = False)
  stroksGreen = db.Column(db.Integer, nullable = False)
  totalShot = db.Column(db.Integer, nullable=False)
  score = db.relationship('ScoresModel', backref='scores', lazy='dynamic')

  def __init__(self, firstClub, firstDistance, secondClub, secondDistance, stroksGreen, totalShot):
    self.firstClub = firstClub
    self.firstDistance =  firstDistance
    self.secondClub = secondClub
    self.secondDistance = secondDistance
    self.stroksGreen = stroksGreen
    self.totalShot = totalShot
  
  @classmethod
  def find_by_id(cls, stat_id):
    return cls.query.filter_by(id=stat_id).first()

  def json(self):
    return {'firstClub': self.firstClub,
            'firstDistance': self.firstDistance, 'secondClub': self.secondClub,
            'secondDistance': self.secondDistance, 'stroksGreen': self.stroksGreen,
            'totalShot': self.totalShot}
  
  def save_to_db(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def update_stat(cls, stat_id, firstClub, firstDistance,
                  secondClub, secondDistance, stroksGreen, totalShot):
    try: 
      updated_stat = cls.query.filter_by(id=stat_id).first()
      updated_stat.firstClub = firstClub
      updated_stat.firstDistance = firstDistance
      updated_stat.secondClub = secondClub
      updated_stat.secondDistance = secondDistance
      updated_stat.stroksGreen = stroksGreen
      updated_stat.totalShot = totalShot
      db.session.commit()
    except SQLAlchemyError as e:
      db.session.rollback()
      print (e) 

  
