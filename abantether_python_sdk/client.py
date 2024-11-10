from typing import Any, Callable, Dict, Optional, Union

import requests

from abantether_python_sdk.client_portocol import ClientProtocol
from abantether_python_sdk.config import config


class Client(ClientProtocol):
    def __init__(self, api_key: Optional[str] = None) -> None:

        self.config: Dict[str, Any] = config
        self.api_key: str = api_key

    def _make_request(
        self,
        endpoint: str,
        params: Optional[Dict[str, Union[str, int]]] = None,
        body: Optional[Dict[str, Any]] = None,
    ) -> Any:
        config: Optional[Dict[str, Any]] = self.config["endpoints"].get(endpoint)
        if not config:
            raise ValueError(f"Endpoint '{endpoint}' not found in configuration.")

        # Validate required parameters
        required_params: list[str] = config.get("required_params", [])
        missing_params: list[str] = [
            p for p in required_params if p not in (params or {})
        ]
        if missing_params:
            raise ValueError(
                f"Missing required parameters: {', '.join(missing_params)}"
            )

        # Build URL with path parameters and add optional params if provided
        url: str = config["url"].format(**params) if params else config["url"]
        headers: Dict[str, str] = {"Authorization": self.api_key}
        method: str = config["method"].upper()

        # Filter params to include both required and optional
        all_params: Dict[str, Any] = {
            **{k: v for k, v in (params or {}).items() if k in required_params},
            **{
                k: v
                for k, v in (params or {}).items()
                if k in config.get("optional_params", [])
            },
        }

        # Make the request and handle errors
        try:
            response: requests.Response = requests.request(
                method=method, url=url, headers=headers, json=body or all_params
            )
            response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            # Display the response text for validation or other HTTP errors
            error_message = (
                f"HTTP error occurred: {http_err}\nResponse Text: {response.text}"
            )
            raise ValueError(error_message) from http_err
        except requests.exceptions.RequestException as req_err:
            # General error in request
            raise ValueError(f"Request error occurred: {req_err}") from req_err

    def __getattr__(self, endpoint_name: str) -> Callable[..., Any]:
        if endpoint_name not in self.config["endpoints"]:
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '{endpoint_name}'"
            )

        def dynamic_method(**kwargs: Any) -> Any:
            return self._make_request(endpoint_name, params=kwargs)

        return dynamic_method
