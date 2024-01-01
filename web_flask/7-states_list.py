#!/usr/bin/python3

'''
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text
variable (replace underscore _ symbols with a space )
'''
from flask import Flask, request, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask("__name__")


@app.route('/states_list', strict_slashes=False)
def display_states():
        '''Renders states_list html page to display states created'''
        states = storage.all()
        return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown(self):
    ''' method that removes the current SQLAlchemy session'''
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
