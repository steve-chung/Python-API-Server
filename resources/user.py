from flask_restful import Resource, reqparse
from models.user import UserModel 
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt


parser = reqparse.RequestParser()
parser.add_argument(
  'email', help='This field cannot be blank', required=True)
parser.add_argument(
  'password', help='This field cannot be blank', required=True)
parser.add_argument(
  'phone', help='This field cannot be blank')
parser.add_argument(
  'name', help='This field cannot be blank')

class UserRegister(Resource):
  def post(self):
    data = parser.parse_args()

    if UserModel.find_by_email(data['email']):
      return {"message": "User already exists, please enter choose different username"}, 400
    new_user = UserModel(
      email = data['email'],
      password = UserModel.generate_hash(data['password']),
      name = data['name'],
      phone = data['phone']
    )
    try:
      new_user.save_to_db()
      access_token = create_access_token(identity=data['email'])
      refresh_token = create_refresh_token(identity=data['email'])
      return {
        'message':'User {} was created'.format(data['name']),
        'access_token': access_token,
        'refresh_token': refresh_token
      }
    except:
      return {"message": "Something went wrong"}, 500


class UserLogin(Resource):
  def post(self):
    data = parser.parse_args()
    current_user = UserModel.find_by_email(data['email'])

    if not current_user:
      return {'message': 'User {} doesn\'t exist'.format(data['email'])}

    if UserModel.verify_hash(data['password'], current_user.password):
      access_token = create_access_token(identity=data['email'])
      refresh_token = create_refresh_token(identity=data['email'])
      return {
        'message': 'Logged in as {}'.format(current_user.name),
        'access_token': access_token,
        'refresh_token': refresh_token
      }
    else:
       return {'message': 'Wrong credentials'}


class TokenRefresh(Resource):
  @jwt_refresh_token_required
  def post(self):
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)
    return {'access_token': access_token}
