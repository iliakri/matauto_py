import json
from os.path import join, dirname, abspath
from jsonschema import validate


class SchemasHelper:

    def __init__(self, app):
        self.app = app

    def assert_valid_schema(self, data, schema_file):
        schema = self.load_json_schema(schema_file)
        return validate(data, schema)

    def load_json_schema(self, filename):
        relative_path = join('../data/schemas', filename)
        absolute_path = join(dirname(__file__), relative_path)

        with open(absolute_path) as schema_file:
            return json.loads(schema_file.read())




