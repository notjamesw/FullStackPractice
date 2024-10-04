from flask import Flask, request, jsonify
from flask_cors import CORS
from collections import deque

app = Flask(__name__)
CORS(app)

# In-memory storage for previous code inputs
cache_size = 10
cache = deque(maxlen = cache_size)
prev_command_index = 0

@app.route('/run_interpreter', methods=['POST'])
def run_interpreter():
    data = request.json
    user_input = data.get('input', '')

    output = interpreter(user_input)

    # Caching the input
    cache.append({'input': user_input})
    prev_command_index = len(cache)-1

    return jsonify({'output': output})

@app.route('/get_prev_command', methods=['GET'])
def get_prev_command():
    if len(cache) == 0:
        return jsonify({'message': 'cannot retrieve prev command, cache is empty'}), 404
    else:
        prev_command = jsonify(cache[prev_command_index])
        if prev_command_index >= 0:
            prev_command_index -= 1
        return prev_command

@app.route('/clear_all_commands', methods=['DELETE'])
def clear_all_commands():
    cache.clear()
    prev_command_index = 0
    return jsonify({'message': 'cache cleared'})
