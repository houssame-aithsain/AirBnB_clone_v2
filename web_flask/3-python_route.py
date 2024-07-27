#!/usr/bin/python3
"""
A simple Flask web application that displays:
- 'Hello HBNB!' on the root route
- 'HBNB' on the /hbnb route
- 'C ' followed by the value of the text variable on the /c/<text> route
- 'Python ' followed by the value of the text variable on the /python/<text>
    route
  (with a default value of 'is cool')
"""
from flask import Flask
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


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Displays 'Python ' followed by the value of the text variable.
    Replaces underscores in the text variable with spaces.
    The default value of text is 'is cool'.
    """
    return "Python " + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
