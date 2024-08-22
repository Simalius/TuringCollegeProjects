import json
import os

class FileManager:
    @staticmethod
    def read_json(filename):
        if not os.path.exists(filename):
            return {}
        with open(filename, 'r') as file:
            return json.load(file)

    @staticmethod
    def write_json(data, filename):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
