from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from dbUtil import *
from flaskAPI import *

app = Flask(__name__)
CORS(app)

api = Api(app)


api.add_resource(getCyberAssets, "/cyberassets")
api.add_resource(deleteCyberAssets, "/cyberassets")