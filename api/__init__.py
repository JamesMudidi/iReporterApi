from flask import Flask
# from flask_cors import CORS
# from app.db import create_tables

# create_tables.create_tables()

app = Flask(__name__)
# CORS(app)

app.url_map.strict_slashes = False

from api.views import users, incident, api

app.register_blueprint(api, url_prefix='/api/v1')