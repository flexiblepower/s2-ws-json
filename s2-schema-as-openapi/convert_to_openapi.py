from pathlib import Path

import json
from typing import Callable, Union

import yaml

JsonType = Union[list["JsonType"], dict[str, "JsonType"],  str,  float,  int,  bool]

def deep_replace(replace_key: str, replace_func: Callable[[str], str], to_inspect: JsonType) -> JsonType:
    if isinstance(to_inspect, dict):
        for key, value in to_inspect.items():
            if key == replace_key:
                to_inspect[key] = replace_func(value)
            else:
                to_inspect[key] = deep_replace(replace_key, replace_func, value)
        return to_inspect
    elif isinstance(to_inspect, list):
        return [replace_func(value) for value in to_inspect]
    else:
        return to_inspect


def convert_ref(old_ref: str) -> str:
    return old_ref.removesuffix('.schema.json') \
                  .replace('../schemas/', '#/components/schemas/') \
                  .replace('.', '_')

def retrieve_version() -> str:
    with open('../s2-asyncapi/s2-cem.yaml') as open_cem_file:
        asyncapi_cem = yaml.safe_load(open_cem_file)
        version = asyncapi_cem['info']['version']
    return version


structures = {}
for file in Path('../s2-json-schema/').glob('**/*.json'):
    if file.is_file():
        with open(file) as open_file:
            print(f'Reading {file}...')
            json_structure = json.load(open_file)

        structures[json_structure['title']] = json_structure

for structure in structures.values():
    del structure['$schema']
    del structure['$id']
    del structure['title']

    if 'properties' in structure:
        structure['properties'] = deep_replace('$ref', convert_ref, structure['properties'])


version = retrieve_version()

openapi_template = {
    'openapi': '3.0.1',
    'info': {
      'title': 'S2 Websocket specification',
      'version': version
    },
    'components': {
        'schemas': structures
    }
}

with open('openapi.yml', 'w+') as open_file:
    yaml.dump(openapi_template,
              open_file,
              width=float("inf"),
              allow_unicode=True)
