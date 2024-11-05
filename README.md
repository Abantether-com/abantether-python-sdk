![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/Abantether-com/abantether-python-sdk/python-app.yml)
![GitHub](https://img.shields.io/github/license/Abantether-com/abantether-python-sdk)

# Abantether Python SDK

A python sdk to trade easily in abantether.com

## How to use?
To install:

```shell
pip install abantether-python-sdk
```

To instantiate the client use:

```python
from abantether_python_sdk.client import Client as AbantetherClient

aban_client = AbantetherClient(access_token=ACCESS_TOKEN)
```
