from bot.orders import place_order
from bot.validators import validate_order
from bot.logging_config import setup_logger
logger = setup_logger()
logger.info(
    "Place order"
)
symbol = input("Symbol: ")
side = input("Side (BUY/SELL): ")
order_type = input(
    "Type (MARKET/LIMIT/STOP): "
)
quantity = input("Quantity: ")


price = None
stop_price = None
if order_type.upper() == "LIMIT":
    price = input("Price: ")

elif order_type.upper() == "STOP":
    stop_price = input("Stop Price: ")
    price = input("Limit Price: ")

order = validate_order(
    symbol,
    side,
    order_type,
    quantity,
    price,
    stop_price
)
logger.info(
    f"Order Request: {symbol} {side} {order_type} {quantity} {price}"
)

response = place_order(symbol,side,order_type,quantity,price)

logger.info(f"Response of Binace {response}")
print("\nOrder Response")
print(response)