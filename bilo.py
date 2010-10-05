def price_generator(ticks):
    current = 1.0
    for i in ticks:
        current *= i
        yield current

class BestReturn(object):
    pass

def find_best_return(ticks, start_date):
    low = high = 1.0
    low_date = high_date = start_date

    best = BestReturn()
    best.low_date = best.high_date = start_date
    best.roi = high/low

    current = 1.0
    for (tick, current_date) in ticks:
        current *= tick

        if current < low:
            # better price, not necessarily better roi
            low = high = current
            low_date = high_date = current_date

        if current == low:
            # same best price, but later date (better return over time)
            low_date = current_date

        if high < current:
            # better high price
            high = current
            new_roi = high / low
            if new_roi > best.roi:
                # better roi, save it
                best.roi = new_roi
                best.low_date = low_date
                best.high_date = current_date

    return best
