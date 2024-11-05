from .enums import Method

base_url = "https://api.abantether.com"

config: dict = {
    "endpoints": {
        "place_market_order": {
            "url": f"{base_url}/order_handler/orders/otc/market",
            "method": Method.POST,
            "required_params": ["side", "base_symbol", "quote_symbol", "volume"],
            "optional_params": [
                "order_type",
                "track_id",
                "payment_source",
                "stop_loss_price",
            ],
        },
        "place_limit_order": {
            "url": f"{base_url}/order_handler/orders/otc/limit",
            "method": Method.POST,
            "required_params": [
                "price",
                "side",
                "base_symbol",
                "quote_symbol",
                "volume",
            ],
            "optional_params": [
                "order_type",
                "track_id",
                "payment_source",
                "stop_loss_price",
            ],
        },
        "sell_all": {
            "url": f"{base_url}/order_handler/orders/otc/limit",
            "method": Method.POST,
            "required_params": ["coins", "currency"],
            "optional_params": [],
        },
        "cancel_order": {
            "url": f"{base_url}/otc/orders/cancel",
            "method": Method.POST,
            "required_params": ["id"],
            "optional_params": [],
        },
        "cancel_stop_order": {
            "url": f"{base_url}/otc/orders/cancel/stop-loss",
            "method": Method.POST,
            "required_params": ["id"],
            "optional_params": [],
        },
        "get_orders": {
            "url": f"{base_url}/order_handler/orders/otc",
            "method": Method.GET,
            "required_params": [],
            "optional_params": [
                "base_symbol",
                "quote_symbol",
                "side",
                "status",
                "order_type",
                "from_date",
                "to_date",
                "quantity_min",
                "quantity_max",
                "track_id",
                "payment_source",
                "page",
                "per_page",
            ],
        },
        "coin_price": {
            "url": f"https://mono.abantether.com/api/v1/otc/coin-price",
            "method": Method.GET,
            "required_params": [],
            "optional_params": ["coin"],
        },
        "balance": {
            "url": f"https://mono.abantether.com/users/balance",
            "method": Method.GET,
            "required_params": [],
            "optional_params": [],
        },
    },

}
