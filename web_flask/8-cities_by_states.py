#!/usr/bin/python3

'''
import and run a web app in flask
'''

from flask import Flask, render_template
from models inport storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    ''' method to close the session '''
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    ''' defines a html page with states and cities '''
    states = storaage.all(State)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
