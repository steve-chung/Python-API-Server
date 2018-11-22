from flask import Flask, jsonify, request
from flask_restful import Api
from yelpapi import YelpAPI
import os
import psycopg2
from config import config
from dotenv import load_dotenv
from resources.user import UserRegister, UserLogin
from flask_jwt_extended import JWTManager
from security import authenticate, identity

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

@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWTManager(app) # this will create /auth
print(jwt)


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

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=PORT, debug=True)
