import time
import hmac
import hashlib
from urllib.parse import urlencode

from bot.client import post
from bot.config import (
    API_key,
    Secret_Key,
    base_url
)


def place_order(
    symbol,
    side,
    order_type,
    quantity,
    price=None,
    stop_price=None
):
    params = {
        "symbol": symbol,
        "side": side,
        
        "quantity": quantity,
        "timestamp": int(time.time() * 1000)
    }
    if order_type == "MARKET":
        params["type"] = "MARKET"
    elif order_type == "LIMIT":
        params["type"] = "LIMIT"
        params["price"] = price
        params["timeInForce"] = "GTC"
    elif order_type == "STOP":

        params["type"] = "STOP"

        params["price"] = price

        params["stopPrice"] = stop_price

        params["timeInForce"] = "GTC"

    query_string = urlencode(params)

    signature = hmac.new(
        Secret_Key.encode(),
        query_string.encode(),
        hashlib.sha256
    ).hexdigest()

    params["signature"] = signature

    headers = {
        "X-MBX-APIKEY": API_key
    }

    return post(
        f"{base_url}/fapi/v1/order",
        headers,
        params
    )