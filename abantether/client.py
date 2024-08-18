from decimal import Decimal
from typing import Dict, Optional, Any

import requests

from abantether.enums import RequestMethod, OrderSide, OrderStatus


class BaseClient:
    # BASE_API_URL = 'https://abantether.com'
    BASE_API_URL = 'https://sandbox.abansite.com'
    BASE_ORDER_URL = f'{BASE_API_URL}/order_handler/orders'
    OTC_ORDERS_URL = f'{BASE_ORDER_URL}/otc'
    PLACE_OTC_MARKET_ORDER_URL = f'{OTC_ORDERS_URL}/market'

    ALL_COINS_URL = f'{BASE_API_URL}/management/all-coins/'

    def __init__(
            self, access_token: Optional[str] = None,
            requests_params: Optional[Dict[str, Any]] = None,
            request_timeout: float = 10,
    ):
        """Abantether API Client constructor

        :param access_token: Access token
        :type access_token: str.
        :param requests_params: optional - Dictionary of requests params to use for all calls
        :type requests_params: dict.
        :param request_timeout: optional - Request timeout in seconds
        :type request_timeout: float.
        """

        self.access_token = access_token
        self.session = self._init_session()
        self.requests_params = requests_params
        self.request_timeout = request_timeout

    def _get_headers(self) -> Dict:
        headers = {
            'Accept': 'application/json',
        }
        if self.access_token:
            headers['Authorization'] = self.access_token
        return headers

    def _init_session(self):
        raise NotImplementedError

    def _request(self, method, url: str, data: Optional[dict] = None):
        raise NotImplementedError

    def _get(self, url: str, data: Optional[dict] = None):
        return self._request(RequestMethod.GET, url, data)

    def _post(self, url: str, data: Optional[dict] = None):
        return self._request(RequestMethod.POST, url, data)

    def _put(self, url: str, data: Optional[dict] = None):
        return self._request(RequestMethod.PUT, url, data)

    def _patch(self, url: str, data: Optional[dict] = None):
        return self._request(RequestMethod.PATCH, url, data)

    def _delete(self, url: str, data: Optional[dict] = None):
        return self._request(RequestMethod.DELETE, url, data)

    def _get_request_params(self, method, data: Optional[dict] = None) -> Dict:
        params = {
            'timeout': self.request_timeout,
        }

        if self.requests_params:
            params.update(self.requests_params)

        if data:
            # Remove any arguments with values of None.
            data = {key: value for key, value in data.items() if value is not None}
            params['data'] = data

        if data and method == RequestMethod.GET:
            params['params'] = '&'.join('%s=%s' % (key, value) for key, value in data.items())
            del params['data']

        return params


class Client(BaseClient):
    def _init_session(self) -> requests.Session:
        headers = self._get_headers()

        session = requests.session()
        session.headers.update(headers)
        return session

    def _request(self, method: str, url: str, data: Optional[dict] = None):
        kwargs = self._get_request_params(method, data)

        self.response = getattr(self.session, method)(url, **kwargs)
        return self._handle_response(self.response)

    @staticmethod
    def _handle_response(response: requests.Response):
        """
        Raises the appropriate exceptions when needed; otherwise, returns the response.
        """
        if not (200 <= response.status_code < 300):
            raise ValueError(f'Request failed with status_code {response.status_code}, Response: {response.text}')
        try:
            return response.json()
        except ValueError:
            raise ValueError(f'Invalid Response: {response.text}')

    # Exchange Endpoints
    def get_all_coins(self, data: Optional[dict] = None) -> Dict:
        """
        Return list of all coins listed on Abantether

        :returns: list - List of coin dictionaries

        .. code-block:: python
        [
        {'symbol': 'BTC', 'name': 'Bitcoin', 'categories': [], 'tetherPrice': '59258.08000000', 'priceBuy': '3466597680.0', 'priceSell': '3442894448.0', 'persianName': 'بیت کوین', 'past24': '1.4189702748584287', 'marketVolume': '1344997464.92907110', 'id': '2', 'active': True, 'irtDecimalPoint': '0', 'tetherDecimalPoint': '2', 'amountDecimalPoint': '9', 'past24volume': '3.06077512915899499483', 'operationStatus': {'buyActive': True, 'sellActive': True, 'withdrawalActive': True, 'depositActive': True, 'transferActive': True}},
        ...
        ]

        """
        coins = self._get(self.ALL_COINS_URL, data)
        return coins

    def get_orders_report(self, side: OrderSide, state: Optional[OrderStatus] = None,
                          base_symbol: Optional[str] = None, quote_symbol: Optional[str] = None,
                          from_date: Optional[str] = None, to_date: Optional[str] = None,
                          quantity_min: Optional[str] = None, quantity_max: Optional[str] = None) -> Dict:
        """
        Return your orders report

        :param side: The side of the order (buy or sell)
        :param base_symbol: optional - The base symbol
        :param quote_symbol: optional - The quote symbol
        :param state: optional - The state of the order
        :param from_date: optional - The start date of the order creation time range - example: 2023-08-25 13:17:08
        :param to_date: optional - The end date of the order creation time range - example: 2023-09-28 13:17:08
        :param quantity_min: optional - The quantity min (IRT or USDT)
        :param quantity_max: optional - The quantity max (IRT or USDT)

        :returns: list - List of order reports

        .. code-block:: python
            TODO

        """

        params = {
            'base_symbol': base_symbol,
            'quote_symbol': quote_symbol,
            'state': state,
            'from_date': from_date,
            'to_date': to_date,
            'side': side,
            'quantity_min': quantity_min,
            'quantity_max': quantity_max,
        }

        return self._get(self.OTC_ORDERS_URL, params)

    def get_order_report(self, order_id: str) -> Dict:
        """
        Return a specific order report

        :param order_id: order_id for the wanted order

        :returns: dict - Report for the specific order

        .. code-block:: python
            TODO

        """

        return self._get(f'{self.BASE_ORDER_URL}/{order_id}')

    def place_market_order(self, base_symbol: str, quote_symbol: str, side: OrderSide,
                           volume: str, track_id: Optional[str] = None,
                           stop_loss_price: Optional[str | Decimal] = None) -> Dict:
        """
        Place a market order

        :param base_symbol: The base symbol
        :param quote_symbol: The quote symbol
        :param side: The side of the order (buy or sell)
        :param volume: The quantity for the order (if buy: volume of quote_symbol, if sell: volume of base_symbol)
        :param track_id: An arbitrary identifier for tracking the order
        :param stop_loss_price: optional - only used when you want to set stop_loss for your order

        :returns: dict - if succeeded, returns the placed order details

        .. code-block:: python
            TODO

        """

        params = {
            'base_symbol': base_symbol,
            'quote_symbol': quote_symbol,
            'side': side,
            'volume': volume,
            'track_id': track_id,
            'stop_loss_price': stop_loss_price,

        }

        return self._post(self.PLACE_OTC_MARKET_ORDER_URL, params)
