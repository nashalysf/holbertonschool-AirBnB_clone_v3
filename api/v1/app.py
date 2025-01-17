#!/usr/bin/python3
"""
Server file for HBNB version 3
"""


from flask import Flask, jsonify, make_response
from models import storage
from api.v1.views import app_views
from flask_cors import CORS


app = Flask(__name__)
# restrictions access for api
CORS(app, resources={r'/api/v1/*': {"origins": "0.0.0.0"}})
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """Closes session"""
    storage.close()


@app.errorhandler(404)
def not_found(exception):
    """Handles 404 error"""
    return make_response(jsonify({'error': "Not found"}), 404)


if __name__ == "__main__":
    """run when invoked"""
    import os
    hoster = os.getenv('HBNB_API_HOST', '0.0.0.0')
    porter = os.getenv('HBNB_API_PORT', '5000')

    app.run(host=hoster, port=porter, threaded=True)
