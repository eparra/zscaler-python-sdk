import sys
import types
import os

# Ensure the package root is on the import path so the SDK can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Provide a minimal stub for the 'httpx' module which is required when importing
# the async client but is not available in the test environment.
httpx_stub = types.ModuleType('httpx')
httpx_stub.AsyncClient = lambda *args, **kwargs: None
sys.modules.setdefault('httpx', httpx_stub)

from zscaler_python_sdk.v2 import ZscalerConfig


def test_base_url_mapping():
    cfg = ZscalerConfig(username='u', password='p', api_key='k', cloud='zscloud')
    assert cfg.get_base_url() == 'https://zsapi.zscloud.net/'


def test_base_url_custom():
    cfg = ZscalerConfig(username='u', password='p', api_key='k', base_url='https://custom/')
    assert cfg.get_base_url() == 'https://custom/'
