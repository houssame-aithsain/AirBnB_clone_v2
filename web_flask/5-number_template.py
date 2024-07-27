#!/usr/bin/python3
"""
A simple Flask web application that displays:
- 'Hello HBNB!' on the root route
- 'HBNB' on the /hbnb route
- 'C ' followed by the value of the text variable on the /c/<text> route
- 'Python ' followed by the value of the text variable on the /python/<text>
    route
  (with a default value of 'is cool')
- 'n is a number' only if n is an integer on the /number/<n> route
- A HTML page with 'Number: n' inside an H1 tag only if n is an integer on the
    /number_template/<n> route
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays 'Hello HBNB!' on the root route.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays 'HBNB' on the /hbnb route.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Displays 'C ' followed by the value of the text variable.
    Replaces underscores in the text variable with spaces.
    """
    return "C " + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """prints Python followed by text"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Displays 'n is a number' only if n is an integer.
    """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Displays a HTML page with 'Number: n' inside an H1 tag only.
    """
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
