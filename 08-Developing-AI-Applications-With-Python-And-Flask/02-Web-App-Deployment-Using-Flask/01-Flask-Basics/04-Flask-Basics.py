# Import the Flask class from the flask module
from flask import Flask, jsonify

# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)

# Define a route for the root URL ('/')
@app.route('/')
def index():
    # Function that handles requests to the root URL
    # Create a dictionary to return as a response
    return jsonify({'message': 'Hello, World!'})


# flask --app server --debug run => in '01-Flask-Basics' folder
# curl -X GET -i -w '\n' localhost:5000 => in cmd
# The -X argument specifies the GET command,
# and the -i argument displays the header from the response.