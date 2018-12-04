from db import db

class StatModel(db.Model):
  __tablename__= 'stat'

  id = db.Column(db.Integer, primary_key=True)
  scores_id = db.Column(db.Integer, db.ForeignKey('scores.id'))
  firstClub = db.Column(db.String(15), nullable = False)
  firstDistance = db.Column(db.Integer, nullable = False)
  secondClub = db.Column(db.String(15), nullable = False)
  secondDistance = db.Column(db.Integer, nullable = False)
  stroksGreen = db.Column(db.Integer, nullable = False)
  totalShot = db.Column(db.Integer, nullable=False)

  def __init__(self, scores_id, firstClub, firstDistance, secondClub, secondDistance, stroksGreen, totalShot)
    self.scores_id = scores_id
    self.firstClub = firstClub
    self.firstDistance =  firstDistance
    self.secondClub = secondClub
    self.secondDistance = secondDistance
    self.stroksGreen = stroksGreen
    self.totalShot = totalShot


  @classmethod
  def find_by_firstClub(cls, scores_id, firstClub)
    return cls.query.filter_by(firstClub=firstClub).first()

  @classmethod
  def find_by_firstDistance(cls, scores_id, firstDistance)
    return cls.query.filter_by(firstDistance=firstDistance).first()

  @classmethod
  def find_by_secondClub(cls, scores_id, secondClub)
    return cls.query.filter_by(secondClub=secondClub).first()

  @classmethod
  def find_by_secondDistance(cls, scores_id, secondDistance)
    return cls.query.filter_by(secondDistance=secondDistance).first()

  @classmethod
  def find_by_stroksGreen(cls, scores_id, stroksGreen)
    return cls.query.filter_by(stroksGreen=stroksGreen).first()

  @classmethod
  def find_by_totalShot(cls, scores_id, totalShot)
    return cls.query.filter_by(totalShot=totalShot).first()

  @classmethod
  def update_firstClub(cls, scores_id, firstClub)
    try:
      cls.session.query.filter(score_id == score_id).update({'firstClub': firstClub})
      session.commit()
    except:
      session.rollback()
      raise

  @classmethod
  def update_firstDistance(cls, scores_id, firstDistance)
    try:
      cls.session.query.filter(score_id == score_id).update({'firstDistance': firstDistance})
      session.commit()
    except:
      session.rollback()
      raise

  @classmethod
  def update_secondClub(cls, scores_id, secondClub)
    try:
      cls.session.query.filter(score_id == score_id).update({'secondClub': secondClub})
      session.commit()
    except:
      session.rollback()
      raise

  @classmethod
  def update_secondDistance(cls, scores_id, secondDistance)
   try:
      cls.session.query.filter(score_id == score_id).update({
                               'secondDistance': secondDistance})
      session.commit()
    except:
      session.rollback()
      raise

  @classmethod
  def update_stroksGreen(cls, scores_id, stroksGreen)
    try:
      cls.session.query.filter(score_id == score_id).update({'stroksGreen': stroksGreen})
      session.commit()
    except:
      session.rollback()
      raise

  @classmethod
  def update_totalScore(cls, scores_id, totalScore)
    try:
      cls.session.query.filter(score_id == score_id).update({'totalScore': totalScore})
      session.commit()
    except:
      session.rollback()
      raise
  
  def save_to_db(self):
    db.session.add(self)
    db.session.commit()

  
