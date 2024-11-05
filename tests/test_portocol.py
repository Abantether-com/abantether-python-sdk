import pytest
import inspect
from typing import get_type_hints
from abantether_python_sdk.client_portocol import ClientProtocol
from abantether_python_sdk.config import config
from typing import Any, Dict

@pytest.mark.parametrize("method_name, endpoint_config", config["endpoints"].items())
def test_protocol_matches_config(method_name, endpoint_config):
    # Get the method from the protocol
    protocol_method = getattr(ClientProtocol, method_name, None)
    assert protocol_method is not None, f"Method '{method_name}' not found in ClientProtocol."

    # Extract method signature
    signature = inspect.signature(protocol_method)
    protocol_params = signature.parameters

    # Check required params
    required_params = endpoint_config["required_params"]
    for param in required_params:
        assert param in protocol_params, f"Required parameter '{param}' missing in '{method_name}' in protocol."

    # Check optional params
    optional_params = endpoint_config["optional_params"]
    for param in optional_params:
        assert param in protocol_params, f"Optional parameter '{param}' missing in '{method_name}' in protocol."

    # Check return type
    return_type = signature.return_annotation
    assert return_type == Dict or return_type == Any, f"Return type for '{method_name}' should be Dict or Any, found {return_type}."


@pytest.mark.parametrize("method_name", [m for m in dir(ClientProtocol) if not m.startswith("_")])
def test_config_matches_protocol(method_name):
    # Ensure each protocol method has an entry in the config
    assert method_name in config["endpoints"], f"Protocol method '{method_name}' is missing in config."
