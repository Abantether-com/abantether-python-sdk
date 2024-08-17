from typing import Dict, Optional, Any

import requests

from enums import RequestMethod


class BaseClient:
    BASE_API_URL = 'https://abantether.com'
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

    def _request(self, method, url: str, **kwargs):
        raise NotImplementedError

    def _get(self, url: str, **kwargs):
        return self._request(RequestMethod.GET.value, url, **kwargs)

    def _post(self, url: str, **kwargs):
        return self._request(RequestMethod.POST.value, url, **kwargs)

    def _put(self, url: str, **kwargs):
        return self._request(RequestMethod.PUT.value, url, **kwargs)

    def _patch(self, url: str, **kwargs):
        return self._request(RequestMethod.PATCH.value, url, **kwargs)

    def _delete(self, url: str, **kwargs):
        return self._request(RequestMethod.DELETE.value, url, **kwargs)


    def _get_request_kwargs(self, method, **kwargs) -> Dict:
        kwargs['timeout'] = self.request_timeout

        if self.requests_params:
            kwargs.update(self.requests_params)

        data = kwargs.get('data', None)
        if data:
            # Remove any arguments with values of None.
            data = {key: value for key, value in data.items() if value is not None}

        if data and method == RequestMethod.GET.value:
            kwargs['params'] = '&'.join('%s=%s' % (key, value) for key, value in data.items())
            del kwargs['data']

        return kwargs


class Client(BaseClient):
    def _init_session(self) -> requests.Session:
        headers = self._get_headers()

        session = requests.session()
        session.headers.update(headers)
        return session

    def _request(self, method:str, url: str, **kwargs):
        kwargs = self._get_request_kwargs(method, **kwargs)
        print('111111111', kwargs['params'])

        self.response = getattr(self.session, method)(url, **kwargs)
        return self._handle_response(self.response)

    @staticmethod
    def _handle_response(response: requests.Response):
        """
        Raises the appropriate exceptions when needed; otherwise, returns the response.
        """
        if not (200 <= response.status_code < 300):
            raise ValueError(f'Request failed: {response.text}')
        try:
            return response.json()
        except ValueError:
            raise ValueError(f'Invalid Response: {response.text}')


    # Exchange Endpoints
    def get_all_coins(self, **kwargs) -> Dict:
        """
        Return list of all coins listed on Abantether

        :returns: list - List of coin dictionaries

        .. code-block:: python
        [
        {'symbol': 'BTC', 'name': 'Bitcoin', 'categories': [], 'tetherPrice': '59258.08000000', 'priceBuy': '3466597680.0', 'priceSell': '3442894448.0', 'persianName': 'بیت کوین', 'past24': '1.4189702748584287', 'marketVolume': '1344997464.92907110', 'id': '2', 'active': True, 'irtDecimalPoint': '0', 'tetherDecimalPoint': '2', 'amountDecimalPoint': '9', 'past24volume': '3.06077512915899499483', 'operationStatus': {'buyActive': True, 'sellActive': True, 'withdrawalActive': True, 'depositActive': True, 'transferActive': True}},
        ...
        ]

        """
        coins = self._get(self.ALL_COINS_URL,**kwargs)
        return coins

    def get_orders_report(self) -> Dict:
        """
        Return your orders report

        :returns: list - List of product dictionaries

        .. code-block:: python


        """

        return self._get(self.OTC_ORDERS_URL)
