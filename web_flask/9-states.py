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


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def state(state_id=None):
	"""The function will display states and city in alphabetical order"""
	state = storage.all("State")
	if state_id is not None:
		state_id = 'State.' + state_id
	return render_template('9-states.html', state=state)

@app.teardown_appcontext
def appcontext_td(exception):
	"""The function will close the storage on the teardown"""
	storage.close()

if __name__ == "__main__":
	app.run(host='0.0.0.0', port='5000')
