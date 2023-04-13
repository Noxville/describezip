from zipfile import ZipFile
from models import Node
import json
import sys
import re


def pprint(nd, depth=0):
    for child_name, child_data in nd.children.items():
        values = ' -> ' + str(child_data) if child_data.data else ''
        print(f"{' ' * 4 * depth}{child_name}{values}")
        pprint(child_data, 1 + depth)


def cull_archive(full_file_name):
    return full_file_name[full_file_name.find('/') + 1:]


def walk_tree(json_obj, parents, n):
    for k, v in json_obj.items():
        if isinstance(v, dict):
            yield from walk_tree(v, parents + [k], n + 1)
        else:
            yield parents + [k], v


def process_zip(filename, file_regex_string="^.*\\.json$"):
    file_regex = re.compile(file_regex_string)
    tree = Node()
    with ZipFile(filename, "r") as zp_file:
        files = {cull_archive(_): _ for _ in zp_file.namelist() if file_regex.match(cull_archive(_))}
        print(f"Loaded {len(files)} files from zip archive {filename}.")

        for cf, f in files.items():
            file_data = zp_file.read(f).decode('utf-8')
            for _path, _value in walk_tree(json.loads(file_data), [], 0):
                tree.traverse(_path).add_value(_value)
        pprint(tree)


if __name__ == "__main__":
    process_zip(*sys.argv[1:])
