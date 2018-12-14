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


  # @classmethod
  # def find_by_firstClub(cls, firstClub):
  #   return cls.query.filter_by(firstClub=firstClub).first()

  # @classmethod
  # def find_by_firstDistance(cls, firstDistance):
  #   return cls.query.filter_by(firstDistance=firstDistance).first()

  # @classmethod
  # def find_by_secondClub(cls, secondClub):
  #   return cls.query.filter_by(secondClub=secondClub).first()

  # @classmethod
  # def find_by_secondDistance(cls, secondDistance):
  #   return cls.query.filter_by(secondDistance=secondDistance).first()

  # @classmethod
  # def find_by_stroksGreen(cls, stroksGreen):
  #   return cls.query.filter_by(stroksGreen=stroksGreen).first()

  # @classmethod
  # def find_by_totalShot(cls, totalShot):
  #   return cls.query.filter_by(totalShot=totalShot).first()

  # @classmethod
  # def update_firstClub(cls, firstClub):
  #   try:
  #     cls.query.filter(scores_id == scores_id).update({'firstClub': firstClub})
  #     cls.commit()
  #   except:
  #     cls.rollback()
  #     raise

  # @classmethod
  # def update_firstDistance(cls, scores_id, firstDistance):
  #   try:
  #     cls.query.filter(scores_id == scores_id).update({'firstDistance': firstDistance})
  #     cls.commit()
  #   except:
  #     cls.rollback()
  #     raise

  # @classmethod
  # def update_secondClub(cls, scores_id, secondClub):
  #   try:
  #     cls.query.filter(scores_id == scores_id).update({'secondClub': secondClub})
  #     cls.commit()
  #   except:
  #     cls.rollback()
  #     raise

  # @classmethod
  # def update_secondDistance(cls, scores_id, secondDistance):
  #   try:
  #     cls.query.filter(scores_id == scores_id).update({
  #                              'secondDistance': secondDistance})
  #     cls.commit()
  #   except:
  #     cls.rollback()
  #     raise

  # @classmethod
  # def update_stroksGreen(cls, scores_id, stroksGreen):
  #   try:
  #     cls.query.filter(scores_id == scores_id).update({'stroksGreen': stroksGreen})
  #     cls.commit()
  #   except:
  #     cls.rollback()
  #     raise

  # @classmethod
  # def update_totalScore(cls, scores_id, totalScore):
  #   try:
  #     cls.query.filter(scores_id == scores_id).update({'totalScore': totalScore})
  #     cls.commit()
  #   except:
  #     cls.rollback()
  #     raise
  
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

  
