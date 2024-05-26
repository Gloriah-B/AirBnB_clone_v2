#!/usr/bin/python3
"""
This script creates a Flask web application with a single route.
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Display 'Hello HBNB!' when the root URL is accessed.
    """
    return 'Hello HBNB!'


if __name__ == "__main__":
    # start the flask development server
    # Listen on all available network interface (0.0.0.0) port 5000
    app.run(host='0.0.0.0', port=5000)
