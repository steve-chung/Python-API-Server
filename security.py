from werkzeug.security import safe_str_cmp
from models.user import UserModel
import hashlib


def authenticate(email, password):
  user = UserModel.find_by_email(email)
  # safe_str_cmp safely compare string no matter what version it is running at
  print(password)
  hashed_password = hashlib.md5(password.encode()).hexdigest()
  
  if user and safe_str_cmp(user.password, hashed_password):
    return user


def identity(payload):
  user_id = payload['identity']
  return UserModel.find_by_id(user_id)
