
class Global(object):
    value_map = {}

    def __init__(self, key='', value: dict={}):
        if key:
            self.set_value(key, value)

    def set_value(self, key, value):
        self.value_map[key] = value

    def __str__(self):
        return str(self.value_map)
        # return self.value_map

    def __getattr__(self, key):
        return self.get_data(key)

    def __getitem__(self, key):
        return self.get_data(key)

    def get_data(self, key):
        if key in self.value_map:
            json_result = self.value_map[key]
            if isinstance(json_result, dict):
                global_result = Global()
                {k: global_result.set_value(k, v) for k, v in json_result.items()}
                return global_result
            else:
                return json_result
        return None

g = Global()
