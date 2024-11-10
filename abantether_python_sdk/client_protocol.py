from typing import List, Protocol, Union, Optional, Dict


class ClientProtocol(Protocol):
    """Abantether API Client for cryptocurrency trading operations.

    This client provides methods to interact with the Abantether API (https://api.abantether.com)
    for placing orders, managing trades, and retrieving account information.
    """
    def place_market_order(
        self,
        side: str,
        base_symbol: str,
        quote_symbol: str,
        volume: Union[str, float],
        order_type: Optional[str] = None,
        track_id: Optional[str] = None,
        payment_source: Optional[str] = None,
        stop_loss_price: Optional[Union[str, float]] = None,
    ) -> Dict: 
        """Place a market order for immediate execution.

        Args:
            side (str): Order side ('buy' or 'sell')
            base_symbol (str): Base currency symbol (e.g., 'BTC')
            quote_symbol (str): Quote currency symbol (e.g., 'USDT')
            volume (float): Order volume in base currency
            **kwargs: Optional parameters including:
                - order_type: Type of the order
                - track_id: Custom tracking identifier
                - payment_source: Source of payment
                - stop_loss_price: Stop loss trigger price

        Endpoint: POST https://api.abantether.com/order_handler/orders/otc/market
        """
        ...

    def place_limit_order(
        self,
        price: Union[str, float],
        side: str,
        base_symbol: str,
        quote_symbol: str,
        volume: Union[str, float],
        order_type: Optional[str] = None,
        track_id: Optional[str] = None,
        payment_source: Optional[str] = None,
        stop_loss_price: Optional[Union[str, float]] = None,
    ) -> Dict: 
        """Place a limit order with a specified price.

        Args:
            price (float): Limit price for the order
            side (str): Order side ('buy' or 'sell')
            base_symbol (str): Base currency symbol (e.g., 'BTC')
            quote_symbol (str): Quote currency symbol (e.g., 'USDT')
            volume (float): Order volume in base currency
            **kwargs: Optional parameters including:
                - order_type: Type of the order
                - track_id: Custom tracking identifier
                - payment_source: Source of payment
                - stop_loss_price: Stop loss trigger price

        Endpoint: POST https://api.abantether.com/order_handler/orders/otc/limit
        """
        ...

    def sell_all(
        self,
        coins: List[str],
        currency: str,
    ) -> Dict: 
        """Sell all holdings for specified coins.

        Args:
            coins (list): List of coin symbols to sell
            currency (str): Currency to sell into

        Endpoint: POST https://api.abantether.com/order_handler/orders/otc/limit
        """

        ...

    def cancel_order(
        self,
        id: str,
    ) -> Dict: 
        """Cancel an existing order.

        Args:
            order_id (str): ID of the order to cancel

        Endpoint: POST https://api.abantether.com/otc/orders/cancel
        """
        ...

    def cancel_stop_order(
        self,
        id: str,
    ) -> Dict: 
        """Cancel an existing stop-loss order.

        Args:
            order_id (str): ID of the stop-loss order to cancel

        Endpoint: POST https://api.abantether.com/otc/orders/cancel/stop-loss
        """
        ...

    def get_orders(
        self,
        base_symbol: Optional[str] = None,
        quote_symbol: Optional[str] = None,
        side: Optional[str] = None,
        status: Optional[str] = None,
        order_type: Optional[str] = None,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        quantity_min: Optional[Union[str, float]] = None,
        quantity_max: Optional[Union[str, float]] = None,
        track_id: Optional[str] = None,
        payment_source: Optional[str] = None,
        page: Optional[int] = None,
        per_page: Optional[int] = None,
    ) -> Dict: 
        """Retrieve order history with optional filters.

        Args:
            **kwargs: Optional filter parameters including:
                - base_symbol: Base currency symbol
                - quote_symbol: Quote currency symbol
                - side: Order side ('buy' or 'sell')
                - status: Order status
                - order_type: Type of order
                - from_date: Start date for order history
                - to_date: End date for order history
                - quantity_min: Minimum order quantity
                - quantity_max: Maximum order quantity
                - track_id: Custom tracking identifier
                - payment_source: Source of payment
                - page: Page number for pagination
                - per_page: Number of orders per page

        Endpoint: GET https://api.abantether.com/order_handler/orders/otc
        """
        ...

    def coin_price(
        self,
        coin: Optional[str] = None,
    ) -> Dict: 
        """Retrieve the price of a specific coin.

        Returns:
            Price information for the specified coin.

        Endpoint: GET https://mono.abantether.com/coins/price
        """
        ...

    def balance(self) -> Dict:
        """Retrieve account balance information.

        Returns:
            Account balance information for all currencies.

        Endpoint: GET https://mono.abantether.com/users/balance
        """
        ...
