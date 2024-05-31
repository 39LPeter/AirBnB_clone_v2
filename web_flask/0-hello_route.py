#!/usr/bin/python3
<<<<<<< HEAD
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
=======
"""Script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hi_hbnb():
    """display “Hello HBNB!” on the terminal"""
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
>>>>>>> 0ff8436f3f691fd58d8b3867ba6f9057ac64e3c1
