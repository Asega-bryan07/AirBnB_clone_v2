#!/usr/bin/python3
''' Start a flask web app '''
from models import storage
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    ''' Shows the main filter page for HBNB '''
    st = storage.all("State")
    amt = storage.all("Amenity")
    return render_template("10-hbnb_filters.html", st=st, amt=amt)


@app.teardown_appcontext
def teardown(exc):
    '''Removes the current SQLAlchemy session'''
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)