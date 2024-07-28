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


@app.route('/states_list', strict_slashes=False)
def state_lists():
	"""The function will display an HTML page in alphabetical order"""
	state = sorted(list(storage.all("State").values()), key=lambda x: x.name)
	return render_template('7-states_list.html', state=state)

@app.teardown_appcontext
def appcontext_td(exception):
	"""The function will close the storage on the teardown"""
	storage.close()
if __name__ == "__main__":
	app.run(host='0.0.0.0', port='5000')
