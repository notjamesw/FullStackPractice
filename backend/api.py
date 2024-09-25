from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory storage for previous code inputs
results = []

@app.route("/run_interpreter", methods=['POST'])
def run_interpreter():
    return 0

@app.route("/get_prev_command", methods=['GET'])
def get_prev_command():
    return 0

@app.route("/clear_all_commands", methods=['DELETE'])
def clear_all_commands():
    return 0
