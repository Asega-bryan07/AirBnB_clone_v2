#!/usr/bin/python3

'''
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text
variable (replace underscore _ symbols with a space )
'''
from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    '''Returns a given string'''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''Returns a given string '''
    return "HBNB!"


@app.route('/c/<text>', strict_slashes=False)
def cText(text):
    '''displays C followed by a value of the text variable'''
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonText(text="is cool"):
    '''returns python followed by the text of the variable'''
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def isNumber(n):
    if isinstance(n, int):
        return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
