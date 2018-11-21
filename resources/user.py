from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('email',
                      type=str,
                      required=True,
                      help="This field cannot be left blank!")
  parser.add_argument('password',
                      type=str,
                      required=True,
                      help="This field cannot be left blank!")
  parser.add_argument('phone',
                      type=str,
                      required=True,
                      help="This field cannot be left blank!")
  def post(self):
    data = UserRegister.parser.parse_args()
    if UserModel.find_by_username(data['email']):
      return {"message": "User already exists, please enter choose different username"}, 400

    user = UserModel(**data)
    user.save_to_db()

    return {"message": "User created successfully."},
