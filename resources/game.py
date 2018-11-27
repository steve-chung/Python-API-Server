from flask_restful import Resource, reqparse
from flask import jsonify
from flask_jwt_extended import get_jwt_identity,  jwt_required
from models.user import UserModel
from models.games import Game
from ast import literal_eval

class PlayGame(Resource):
