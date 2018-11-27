from flask import Flask, jsonify, request
from flask_restful import Api
from yelpapi import YelpAPI
import os
import psycopg2
from config import config
from dotenv import load_dotenv
from resources.user import UserRegister, UserLogin, TokenRefresh, UserLogout
from resources.reserve import reserveCourse
from resources.holes import createHoles
from flask_jwt_extended import JWTManager
from models.user import RevokedTokenModel


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
yelp_api_key = os.getenv('YELPKEY')
PORT = os.getenv('PORT')
yelp_api = YelpAPI(yelp_api_key)




app = Flask(__name__)

app.secret_key = os.getenv('JWTKEY')
api = Api(app)
params = config()
url = 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
url = url.format(**params)
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWTManager(app) # this will create /auth

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    return RevokedTokenModel.is_jti_blacklisted(decrypted_token['jti']) 

@jwt.expired_token_loader
def expired_token_callback():
    return jsonify({
        'description': 'The token has expired',
        'error': 'token_expired'
    }), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        'description': 'Signature verification failed',
        'error': 'invalid_token'
    }), 401

@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        'description': 'Request does not contain an access token.',
        'error': 'authorization_required'
    }), 401

@jwt.needs_fresh_token_loader
def token_not_fresh_callback():
    return jsonify({
        'description': 'The token is not fresh.',
        'error': 'fresh_token_required'
    }), 401

@jwt.revoked_token_loader
def revoked_token_callback():
    return jsonify({
        'description': 'The token has been revoked.',
        'error':'token_revoked'
    }), 401


@app.errorhandler(500)
def server_error(error=None):
    message = {
        'status': 500,
        'message': 'Internal Server Error' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 500

    return resp

@app.route('/api/courses')
def yelp_get_data():
    lat = request.args.get('lat')
    lng = request.args.get('lng')

    response = yelp_api.search_query(
            latitude = lat,
            longitude = lng,
            radius = 25000,
            categories = 'golf',
            sort_by = 'distance'
    )
    if response :
        return jsonify(response)
    return server_error()

api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(TokenRefresh, '/refresh')
api.add_resource(UserLogout, '/logout')
api.add_resource(reserveCourse, '/reserve')
api.add_resource(createHoles, '/holes')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=PORT, debug=True)
