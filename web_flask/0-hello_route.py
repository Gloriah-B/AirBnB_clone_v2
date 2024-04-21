#!/usr/bin/python3
"""
This script creates a Flask web application with a single route.
"""

from flask import Flask

app = Flask(__name__)


# Define the route for the root URL '/'
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Display 'Hello HBNB!' when the root URL is accessed.
    """
    return 'Hello HBNB!'


if __name__ == "__main__":
    # start the flask development server
    # Listen on all available network interface (0.0.0.0) port 5000
    app.run(host='0.0.0.0', port=5000)
