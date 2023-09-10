#!/usr/bin/python3
"""Flask Main serve App"""

from flask import Flask
from flask import abort, render_template, jsonify, Config
from flask_cors import CORS
import os
app = Flask(__name__)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
app.register_blueprint(app_views)




@app.errorhandler(404)
def not_found():
    """Returns not found error if no content"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    
    host = os.getenv("HOST", "0.0.0.0")
    port = os.getenv("PORT", "5000")
    app.run(host=host, port=port, debug=True)