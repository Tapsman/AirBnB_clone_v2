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

if __name__ == "__main__":
	app.run(host='0.0.0.0', port='5000')
