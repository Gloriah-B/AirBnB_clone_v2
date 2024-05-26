#!/usr/bin/python3

    """
    Start web application with two routings
    """

from flask import Flask, render_template
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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """
    Display 'Python ' followed by the value of the text variable.
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def isanumber(n):
    """
    Display 'n is a number' if n is an integer.
    """
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=false)
def number_template(n):
    """Retrieve template for request
    """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
