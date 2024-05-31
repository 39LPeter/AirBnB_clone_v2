#!/usr/bin/python3
<<<<<<< HEAD
"""
starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'

if __name__ == '__main__':
=======
"""Script that prepares a Flask web app"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hi_hbnb():
    """display “Hello HBNB!” on the terminal"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Display HBNB"""
    return 'HBNB'

if __name__ == "__main__":
>>>>>>> 0ff8436f3f691fd58d8b3867ba6f9057ac64e3c1
    app.run(host='0.0.0.0', port='5000')
