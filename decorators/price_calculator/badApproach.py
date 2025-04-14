def calculate_price(price, seasonal=False, promo_code=None, loyalty=None, quantity=1):

    if price < 0:

        raise ValueError("Price cannot be negative")

    # Seasonal discount

    if seasonal:

        price -= price * 0.10

    # Promo code logic

    if promo_code == "SAVE5" and price >= 50:

        price -= 5

    # Loyalty-based percentage discount

    if loyalty == "bronze":

        price -= price * 0.05

    elif loyalty == "silver":

        price -= price * 0.075

    elif loyalty == "gold":

        price -= price * 0.10

    # Bulk discount

    if quantity >= 10:

        price -= price * 0.15

    # Tax (8.25%)

    price += price * 0.0825

    return max(0, price)
