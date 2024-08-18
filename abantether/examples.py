from client import Client as AbantetherClient
from enums import OrderSide
from pandas.io.formats.format import return_docstring

ACCESS_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI3MDIiLCJpYXQiOjE3MjM5NzgxNTkuNzM2NTg4NywiZXhwIjoxNzIzOTgxNzU5LCJzZXNzaW9uX2lkIjoiMzhiNzgwMjktNThiNS00MjQzLTk3ZDctNDYxZDQ4OTg3MzYwIiwidHlwZSI6IkxPR0lOIiwicmVxdWlyZWRfbGF5ZXJzIjp7InBhbmVsIjp7ImRpZmYiOltdLCJ1c2VfcG9saWN5IjoiQUxXQVlTIiwiYWN0aXZlIjp7fX0sIndpdGhkcmF3YWwiOnsiZGlmZiI6WyJhdXRoZW50aWNhdG9yIl0sInVzZV9wb2xpY3kiOiJSRVNFVCIsImFjdGl2ZSI6e319LCJ3aGl0ZWFkZHJlc3MiOnsiZGlmZiI6WyJhdXRoZW50aWNhdG9yIiwiZW1haWwtb3RwIl0sInVzZV9wb2xpY3kiOiJFWFBJUkUiLCJhY3RpdmUiOnt9fSwiYXBpX2tleV9hY3RpdmF0ZSI6eyJkaWZmIjpbImF1dGhlbnRpY2F0b3IiLCJwaG9uZS1vdHAiXSwidXNlX3BvbGljeSI6IlJFU0VUIiwiYWN0aXZlIjp7fX19fQ.3N_Pxgo1SSKhBkjrKtozb6lEUeGzJs7QlOW7sgfZcHE'


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
        # track_id='9832nd9823b9',
        # stop_loss_price='',
    )
    return order_info


if __name__ == '__main__':
    print(place_market_order())
