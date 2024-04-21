#!/usr/bin/python3
"""
This script creates a Flask web application with five routes.
"""

from flask import Flask, abort
from urllib.parse import unquote

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


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    """
    Display 'C ' followed by the value of the text variable.
    Replace underscore _ symbols with a space.
    """
    text = unquote(text)  # Decode URL-encoded text
    text = text.replace('_', ' ')  # Replace underscores with spaces
    return 'C {}'.format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text):
    """
    Display 'Python ' followed by the value of the text variable.
    If no text is provided, use 'is cool' as the default.
    """
    text = unquote(text)  # Decode URL-encoded text
    text = text.replace('_', ' ') if text else 'is cool'
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """
    Display 'n is a number' if n is an integer.
    Otherwise, return a 404 error.
    """
    if isinstance(n, int):
        return '{} is a number'.format(n)
    else:
        abort(404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
