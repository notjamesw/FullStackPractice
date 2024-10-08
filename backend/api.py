from flask import Flask, request, jsonify
from flask_cors import CORS
from collections import deque
from program.main import interpreter

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
        self.interpreter = interpreter()

    def run(self):
        self.app.run(debug=True)

    def run_interpreter(self):
        data = request.json
        user_input = data.get('input', '')

        # Caching the input
        self.cache.append(user_input)
        self.prev_command_index = len(self.cache) - 1
        
        output = self.interpreter.program(user_input)
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

if __name__ == '__main__':
    api = InterpreterAPI()
    api.run()
