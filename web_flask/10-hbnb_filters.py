#!/usr/bin/python3
""" module numbr roote"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models import *
from models.city import City
from models.amenity import Amenity


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ def hellowww """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ def hbnb """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ def c """
    return "C {}".format(text.replace("_", " "))


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """ def python """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ def number """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ def number template """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """ def number template """
    if n % 2 == 0:
        answer = "even"
    else:
        answer = "odd"
    return render_template('6-number_odd_or_even.html', n=n, answer=answer)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ def doc """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ def doc """
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states(id=None):
    """ def states """
    states = storage.all(State)
    if id is not None:
        id = "State." + id
    return render_template("9-states.html", states=states, state_id=id)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """ def hbnb """
    states = storage.all(State)
    Amenties = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', states=states,
                           Amenties=Amenties)


@app.teardown_appcontext
def tear_db(e):
    """ tear db """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
