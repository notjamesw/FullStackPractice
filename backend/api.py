from flask import Flask, request, jsonify
from flask_cors import CORS
from collections import deque


class InterpreterAPI:
    cache_size = 10

    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app)
        self.cache = deque(maxlen = self.cache_size)
        self.prev_command_index = 0
        self.app.add_url_rule('/run_interpreter', 'run_interpreter', self.run_interpreter, methods=['POST'])
        self.app.add_url_rule('/get_prev', 'get_prev', self.get_prev, methods = ['GET'])
        self.app.add_url_rule('/clear_all', 'clear_all', self.clear_all_commands, methods = ['DELETE'])

    def run(self):
        self.app.run(debug=True)

    def run_interpreter(self):
        data = request.json
        user_input = data.get('input', '')

        # Caching the input
        self.cache.append(user_input)
        self.prev_command_index = len(self.cache) - 1
        print(self.cache[self.prev_command_index])

        output = interpreter(user_input)
        return jsonify({'output': output})
    
    def get_prev(self):
        if len(self.cache) == 0:
            return jsonify({'message': 'cannot retrieve prev command, cache is empty'}), 404
        else:
            print(self.prev_command_index)
            prev_command = jsonify({'output': self.cache[self.prev_command_index]})
            if self.prev_command_index > 0:
                self.prev_command_index -= 1
            return prev_command
    
    def clear_all_commands(self):
        self.cache.clear()
        self.prev_command_index = 0
        return jsonify({'message': 'cache cleared'})

def interpreter(input):
    return input + " test interp"


if __name__ == '__main__':
    api = InterpreterAPI()
    api.run()

'''
@app.route('/run', methods=['POST'])
def run_interpreter():
    data = request.json
    user_input = data.get('input', '')

    output = interpreter(user_input)
    print("working interp")
    # Caching the input
    cache.append({'input': user_input})
    prev_command_index = len(cache)-1
    print("cache success")

    return jsonify({'output': output})

@app.route('/get_prev', methods=['GET'])
def get_prev():
    if len(cache) == 0:
        return jsonify({'message': 'cannot retrieve prev command, cache is empty'}), 404
    else:
        prev_command = jsonify(cache[prev_command_index])
        if prev_command_index >= 0:
            prev_command_index -= 1
        return prev_command

@app.route('/clear_all', methods=['DELETE'])
def clear_all_commands():
    cache.clear()
    prev_command_index = 0
    return jsonify({'message': 'cache cleared'})
'''