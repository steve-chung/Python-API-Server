from db import db

class UserModel(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(80))
  password = db.Column(db.String(100))
  phone = db.Column(db.String(15))
  def __init__(self, email, password, phone):
    self.email = email
    self.password = password
    self.phone = phone

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()

  @classmethod

  def find_by_username(cls, email):
 
    return cls.query.filter_by(email=email).first()
