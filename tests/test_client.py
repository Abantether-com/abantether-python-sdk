import pytest
from unittest.mock import patch, Mock
from abantether_python_sdk.client import Client
import requests


@pytest.fixture
def client():
    return Client(api_key="test_api_key")


@patch("requests.request")
def test_make_request_success(mock_request, client):
    # Arrange: Mock a successful response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"status": "success"}
    mock_request.return_value = mock_response

    # Act: Call the method
    response = client._make_request(
        endpoint="place_market_order",
        params={
            "side": "buy",
            "base_symbol": "BTC",
            "quote_symbol": "USDT",
            "volume": "0.001",
        },
    )

    # Assert
    assert response == {"status": "success"}
    mock_request.assert_called_once_with(
        method="POST",
        url="https://api.abantether.com/order_handler/orders/otc/market",
        headers={
            "Authorization": "test_api_key"
        },  # ensure this matches your Client code's API key usage
        json={
            "side": "buy",
            "base_symbol": "BTC",
            "quote_symbol": "USDT",
            "volume": "0.001",
        },
    )


@patch("requests.request")
def test_make_request_missing_required_params(mock_request, client):
    # Act and Assert
    with pytest.raises(
        ValueError,
        match="Missing required parameters: side, base_symbol, quote_symbol, volume",
    ):
        client._make_request(endpoint="place_market_order")


@patch("requests.request")
def test_make_request_nonexistent_endpoint(mock_request, client):
    # Act and Assert
    with pytest.raises(
        ValueError, match="Endpoint 'nonexistent_endpoint' not found in configuration."
    ):
        client._make_request(endpoint="nonexistent_endpoint")


@patch("requests.request")
def test_make_request_http_error(mock_request, client):
    # Arrange: Mock an HTTP error response
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(
        "500 Server Error"
    )
    mock_response.status_code = 500
    mock_response.text = "Internal Server Error"
    mock_request.return_value = mock_response

    # Act and Assert
    with pytest.raises(ValueError, match="HTTP error occurred:"):
        client._make_request(
            endpoint="place_market_order",
            params={
                "side": "buy",
                "base_symbol": "BTC",
                "quote_symbol": "USDT",
                "volume": "0.001",
            },
        )


def test_invalid_api_key():
    with pytest.raises(ValueError, match="API key must not be empty"):
        Client(api_key="")


@patch("requests.request")
def test_empty_response_handling(mock_request, client):
    # Arrange: Mock an empty response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = None
    mock_request.return_value = mock_response

    # Act
    response = client._make_request(
        endpoint="place_market_order",
        params={
            "side": "buy",
            "base_symbol": "BTC",
            "quote_symbol": "USDT",
            "volume": "0.001",
        },
    )

    # Assert
    assert response is None


def test_nonexistent_dynamic_method(client):
    # Act and Assert
    with pytest.raises(
        AttributeError, match="object has no attribute 'nonexistent_method'"
    ):
        client.nonexistent_method()
