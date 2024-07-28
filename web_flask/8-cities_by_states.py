#!/usr/bin/python3
"""
This is a script that starts a Flask web application
And it listens on port 5000
"""

import flask
from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def state_by_cities():
	"""The function will display the list in alphabetical order"""
	state = sorted(list(storage.all("State").values()
	return render_template('8-states_list.html', state=state)

@app.teardown_appcontext
def appcontext_td(exception):
	"""The function will close the storage on the teardown"""
	storage.close()

if __name__ == "__main__":
	app.run(host='0.0.0.0', port='5000')
