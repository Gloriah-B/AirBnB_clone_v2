#!/usr/bin/python3
"""
This script creates a Flask web application with two routes.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Display 'Hello HBNB!' when the root URL is accessed.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """
    Display 'HBNB' when /hbnb is accessed.
    """
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
