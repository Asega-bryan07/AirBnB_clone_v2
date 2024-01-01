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


@app.route('/states', strict_slashes=False)
def states():
    ''' defines a html page with states '''
    states = storaage.all(State)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id):
    ''' display html page with cities of the state '''
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', states=state, mode='id')
    return render_template('9-states.html', states=state, mode='none')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
