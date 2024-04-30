"""
This module defines a simple Flask application.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    """
    Handle the root route request.

    Returns:
        str: A greeting message.
    """
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()
