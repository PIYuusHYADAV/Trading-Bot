import requests

from .logging_config import setup_logger
logger = setup_logger()

def post(url, headers, params):
    logger.info(f"Sending request to Binance {params}")
    return requests.post(
        url,
        headers=headers,
        params=params
    ).json()