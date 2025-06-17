"""
Main application entry point.
Initializes the Flask app and sets up the routes.
"""

from flask import Flask, render_template
from controllers.hello_controller import hello_world

# Create Flask application instance
app = Flask(__name__, template_folder='views')

# Register route for the home page
app.add_url_rule("/", "home", hello_world)

# Run the app on 0.0.0.0 to allow external access (Docker)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
