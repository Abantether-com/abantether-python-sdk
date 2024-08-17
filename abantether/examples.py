from client import Client as AbantetherClient
from enums import OrderSide

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
    orders_reports = aban_client.get_orders_report(side=OrderSide.SELL)
    return orders_reports


if __name__ == '__main__':
    print(get_orders_report())
