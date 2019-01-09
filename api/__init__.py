from flask import Flask
from config import app_configuration

app=Flask(__name__)


from api.views import incident_views
from api.views import user_views