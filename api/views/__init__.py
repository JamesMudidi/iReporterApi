from flask import Blueprint
from flask_swagger_ui import get_swaggerui_blueprint


app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
swagger_blueprint = get_swaggerui_blueprint(SWAGGER_URL='api/v2/docs', API_URL='https://app.swaggerhub.com/apis-docs/JamesMudidi/iRepoter/2.0'
api = Blueprint('api', __name__)
