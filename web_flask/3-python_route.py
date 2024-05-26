#!/usr/bin/python3
"""
This script creates a Flask web application with four routes.
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Display 'Hello HBNB!' when the root URL is accessed.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Display 'HBNB' when /hbnb is accessed.
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Display 'C ' followed by the value of the text variable.
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Display 'Python ' followed by the value of the text variable.
    Replace underscore _ symbols with a space.
    If no text is provided, use 'is cool' as the default.
    """
    return 'Python ' + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
