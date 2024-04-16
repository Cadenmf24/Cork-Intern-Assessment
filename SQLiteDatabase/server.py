from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from dbUtil import *
from flaskAPI import *

app = Flask(__name__)
CORS(app)

api = Api(app)


api.add_resource(Getcyberassets, "/cyberassets")
api.add_resource(Deletecyberassets, "/cyberassets")

if __name__ == '__main__':
    print("Loading db")
    exec_sql_file('schema.sql')
    print("starting flask")

    app.run(debug=True)