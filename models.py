from collections import Counter


class Node:
    def __init__(self):
        self.data = list()
        self.children = dict()

    def traverse(self, path):
        if not len(path):
            return self
        if path[0] not in self.children:
            self.children[path[0]] = Node()
        return self.children[path[0]].traverse(path[1:])

    def add_value(self, value):
        self.data.append(value)

    def __repr__(self):
        unique = [_ for _ in list(set(self.data))]
        types = list(set([str(type(_)).replace("<class '", "").replace("'>", "") for _ in unique]))
        obj_type = types[0] if len(types) == 1 else 'mixed'

        match obj_type:
            case 'int' | 'float':
                description = describe_int(self.data, unique)
            case 'str':
                description = describe_str(self.data)
            case 'bool':
                description = describe_bool(self.data)
            case 'mixed':
                description = str(types)
            case _:
                raise Exception(f"Unknown type {obj_type}")

        return f"[{obj_type}] {description}"


def describe_int(values, uniques):
    if len(uniques) <= 10:
        return f"all = {str(uniques)}"

    _min, _max, _avg = None, None, 0
    for idx, val in enumerate(values):
        if idx == 0:
            _min, _max, _avg = val, val, float(val) / len(values)
        else:
            _min = min(_min, val)
            _max = max(_max, val)
            _avg += float(val) / len(values)
    return f"min={_min}, avg={int(_avg * 100) / 100}, max={_max}, count={len(values)}, count_unique={len(uniques)}"


def describe_str(values):
    return str(dict(Counter(values)))


def describe_bool(values):
    return str(dict(Counter(values)))
