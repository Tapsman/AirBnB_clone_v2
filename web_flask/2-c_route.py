#!/usr/bin/python3
"""
This is a script that starts a Flask web application
And it listens on port 5000
"""

import flask
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hail():
	"""The function returns Hello HBNB!"""
	return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
        """The function returns HBNB"""
        return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
        """This is a function to display C, with value of text"""
        return 'C ' + text.replace('_', ' ')

if __name__ == "__main__":
	app.run(host='0.0.0.0', port='5000')
