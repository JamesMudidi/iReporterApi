# Import neccessary depencies
# From the module or framework, we import the class datatype.
from flask import Flask, jsonify, request
import json
from api.views import incident_views
from api.views import user_views

app = Flask(__name__)

# Default error page
@app.errorhandler(404)

# Defining what displays in the default route
def page_not_found(e):
    valid_urls = {
        '1. Create a RedFlag': {'url': '/api/v1/red-flags',
                'method(s)': 'POST', 'body': {'createdBy': 'String',
                'incident_type': 'String', 'location': 'Lat Long', 'status': 'String', 
                'image': 'Image', 'video': 'Video', 'comment': 'string'}},
        '2. View all RedFlags': {'url': '/api/v1/red-flags',
                'method(s)': 'GET', },
        '3. View a single RedFlag': {'url': '/api/v1/red-flags/<int:_id',
                'method(s)': 'GET', },
        '4. Patch a RedFlag comment': {'url': '/api/v1/red-flags/<int:_id>/comment',
                'method(s)': 'PATCH', 'body': {'location': 'Lat Long'}},
        '5. Patch a RedFlag location': {'url': '/api/v1/red-flags/<int:_id>/location',
                'method(s)': 'PATCH', 'body': {'comment': 'string'}},
        '6. Delete a RedFlag': {'url': 'api/v1/red-flag/<int:_id>',
                'method(s)': 'DELETE', },
    }
    return jsonify ({
        '1. Hello': 'Welcome to the iRepoter API',
        '3. Contact': 'For further assistance contact James Mudidi on mudidi.jimmy@gmail.com.',
        '3. Usage': 'Use the links below to navigate through the API',
        '6. Valid_Urls for the site': valid_urls,
        '4. Message': 'Please contact iRepoter for more details on this API.',
        '2. Support': 'You will have to view this site with a JSON Formatter for better results',
       })
