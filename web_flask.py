#!/usr/bin/python3
"""
Imports the Flask class from the flask module.
Creates a Flask application instance named app.
Defines a route for the root URL (/) that returns a simple message.
Runs the Flask application when the script is executed directly.
"""
from flask import Flask

# Create the Flask application instance
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def hello():
    return 'Hello, World!'

# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
