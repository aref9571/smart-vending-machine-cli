def calculate_change(amount: float, reserve: dict):

    coins = sorted(reserve.keys(), reverse=True)

    result = {}

    remaining = round(amount, 2)

    for coin in coins:

        coin_value = coin / 100

        needed = int(remaining // coin_value)

        if needed <= 0:
            continue

        available = reserve[coin]

        used = min(needed, available)

        if used > 0:
            result[coin] = used
            remaining = round(remaining - coin_value * used, 2)

    if remaining != 0:
        raise ValueError("Machine cannot provide change")

    return result
