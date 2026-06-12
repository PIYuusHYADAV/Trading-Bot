def validate_order(
    symbol,
    side,
    order_type,
    quantity,
    price=None,
    stop_price=None
):
    if not symbol:
        raise ValueError(
            "Symbol cannot be empty"
        )

    symbol = symbol.upper()

    side = side.upper()

    if side not in ["BUY", "SELL"]:
        raise ValueError(
            "Side must be BUY or SELL"
        )

    order_type = order_type.upper()

    if order_type not in [
        "MARKET",
        "LIMIT"
        "STOP"
    ]:
        raise ValueError(
             "Order type must be MARKET, LIMIT or STOP"
        )

    try:
        quantity = float(quantity)
    except ValueError:
        raise ValueError(
            "Quantity must be a number"
        )

    if quantity <= 0:
        raise ValueError(
            "Quantity must be greater than 0"
        )

    if order_type == "LIMIT":

        if price is None:
            raise ValueError(
                "Price is required for LIMIT orders"
            )

        try:
            price = float(price)
        except ValueError:
            raise ValueError(
                "Price must be a number"
            )

        if price <= 0:
            raise ValueError(
                "Price must be greater than 0"
            )
    if order_type == "STOP":

        if stop_price is None:
            raise ValueError(
                "Stop price is required"
            )

        stop_price = float(stop_price)

        if stop_price <= 0:
            raise ValueError(
                "Stop price must be positive"
            )

    return {
        "symbol": symbol,
        "side": side,
        "order_type": order_type,
        "quantity": quantity,
        "price": price,
        "stop_price": stop_price
    }