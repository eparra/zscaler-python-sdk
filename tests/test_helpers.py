import sys
import types
import os

# Ensure the package root is on the import path so the SDK can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Provide a minimal stub for the 'requests' module which is required when
# importing the package but is not available in the test environment.
requests_stub = types.ModuleType('requests')
requests_stub.Session = lambda *args, **kwargs: None
sys.modules.setdefault('requests', requests_stub)

from zscaler_python_sdk.Helpers import Helpers


def test_extract_values_nested():
    helper = Helpers()
    helper.debug = False
    data = {
        'a': 1,
        'b': [
            {'a': 2},
            {'c': {'a': 3}}
        ],
        'c': {
            'a': 4,
            'd': [
                {'a': 5},
                6
            ]
        }
    }
    assert helper.extract_values(data, 'a') == [1, 2, 3, 4, 5]


def test_extract_id_from_response_dict():
    helper = Helpers()
    helper.debug = False
    assert helper.extract_id_from_response({'id': 123}) == 123


def test_extract_id_from_response_json_string():
    helper = Helpers()
    helper.debug = False
    json_str = '{"id": 456}'
    assert helper.extract_id_from_response(json_str) == 456
