from flask import Flask, jsonify, request
from flask_restful import Api
from yelpapi import YelpAPI
import os
from dotenv import load_dotenv

# from flask_jwt import JWT


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
yelp_api_key = os.getenv('YELPKEY')
PORT = os.getenv('PORT')
yelp_api = YelpAPI(yelp_api_key)

# from security import authenticate, identity
# from resources.user import UserRegister
# from resources.item import Item, ItemList
# from resources.store import Store, StoreList

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['PROPAGATE_EXCEPTIONS'] = True
# app.secret_key = 'jose'
api = Api(app)

@app.errorhandler(500)
def server_error(error=None):
    message = {
        'status': 500,
        'message': 'Internal Server Error' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 500

    return resp

# @app.before_first_request
# def create_tables():
#     db.create_all()

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
    
# jwt = JWT(app, authenticate, identity)  # /auth

# api.add_resource(Store, '/store/<string:name>')
# api.add_resource(StoreList, '/stores')
# api.add_resource(Item, '/item/<string:name>')
# api.add_resource(ItemList, '/items')
# api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    # from db import db
    # db.init_app(app)
    app.run(port=PORT, debug=True)
