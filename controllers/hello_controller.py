"""
Controller layer of the application.
Handles incoming requests and coordinates responses.
"""

from flask import render_template
from models.hello import get_hello_message

def hello_world():
    """
    Handles the '/' route and renders the Hello World message.
    """
    message = get_hello_message()  # Get message from the model
    return render_template("index.html", message=message)
