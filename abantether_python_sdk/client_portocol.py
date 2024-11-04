from typing import List, Protocol, Union, Optional, Any, Dict


class ClientProtocol(Protocol):
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
    ) -> Dict: ...

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
    ) -> Dict: ...

    def sell_all(
        self,
        coins: List[str],
        currency: str,
    ) -> Dict: ...

    def cancel_order(
        self,
        id: str,
    ) -> Dict: ...

    def cancel_stop_order(
        self,
        id: str,
    ) -> Dict: ...

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
    ) -> Dict: ...

    def coin_price(
        self,
        coin: Optional[str] = None,
    ) -> Dict: ...

    def balance(self) -> Any: ...
