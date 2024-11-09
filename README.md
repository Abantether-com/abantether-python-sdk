![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/Abantether-com/abantether-python-sdk/python-app.yml)
![Codecov](https://img.shields.io/codecov/c/github/Abantether-com/abantether-python-sdk)
![GitHub](https://img.shields.io/github/license/Abantether-com/abantether-python-sdk)
![Python Versions](https://img.shields.io/pypi/pyversions/abantether-python-sdk)
![PyPI Version](https://img.shields.io/pypi/v/abantether-python-sdk)

# Abantether Python SDK

A Python SDK for seamless integration with the [Abantether](https://abantether.com) cryptocurrency trading platform. This SDK provides an easy-to-use interface for executing trades and managing your account on [abantether.com](https://abantether.com).

## Installation

Install the package using pip:

```shell
pip install abantether-python-sdk

# or using uv
uv install abantether-python-sdk
```

To instantiate the client use:

```python
from abantether_python_sdk.client import Client as AbantetherClient

aban_client = AbantetherClient(access_token=ACCESS_TOKEN)
```

## Development

To contribute to this project:

1. Clone the repository
2. Install development dependencies:

```shell
uv sync
```

3. Run tests:
```shell
uv run pytest 
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
