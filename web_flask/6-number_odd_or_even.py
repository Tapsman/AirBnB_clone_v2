#!/usr/bin/python3
"""
This is a script that starts a Flask web application
And it listens on port 5000
"""

import flask
from flask import Flask, render_template
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
def c_fun(text):
        """This is a function to display C, with value of text"""
        return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_cool(text='is_cool'):
        """This is function to display python is cool"""
        return 'Python ' + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def isanumber(n):
        """Displays n is an integer if n is an int"""
        return "{:} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numsandtemplates(n):
        """The function displays an HTML page only if n is an integer"""
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numsandtemplates(n):
        """
	The function displays an HTML page only if n is an integer
	Using the evenness function for distribution, python.
	"""
	if n % 2 == 0:
		evenness = 'even'
	else:
		evenness = 'odd'
        return render_template('6-number_odd_or_even.html', n=n,
				evenness=evenness)
if __name__ == "__main__":
	app.run(host='0.0.0.0', port='5000')
