# Import neccessary depencies
# From the module or framework, we import the class datatype.
from flask import Flask

app = Flask(__name__)

from api.views import index
# from api.views import user_view
