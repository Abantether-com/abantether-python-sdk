from abantether_python_sdk.client import Client as AbantetherClient
from enums import OrderSide
from pandas.io.formats.format import return_docstring

ACCESS_TOKEN = ''


def get_all_coins_details():
    params = {
        'active': True,
    }
    aban_client = AbantetherClient(access_token=ACCESS_TOKEN)
    all_coins_details = aban_client.get_all_coins(data=params)
    return all_coins_details


def get_coin_details(coin_symbol: str):
    all_coins_details = get_all_coins_details()
    for coin_detail in all_coins_details:
        if coin_detail['symbol'] == coin_symbol:
            return coin_detail


def get_orders_report():
    aban_client = AbantetherClient(access_token=ACCESS_TOKEN)
    orders_reports = aban_client.get_orders_report(side=OrderSide.BUY.value)
    return orders_reports


def place_market_order():
    aban_client = AbantetherClient(access_token=ACCESS_TOKEN)
    order_info = aban_client.place_market_order(
        base_symbol='BAT',
        quote_symbol='IRT',
        side='buy',
        volume='700000', # 700,000 Toman
        # track_id='',
        # stop_loss_price='',
    )
    return order_info


if __name__ == '__main__':
    print(place_market_order())
