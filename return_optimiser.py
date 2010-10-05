class BestReturn(object):
    def __init__(self, start_date):
        self.roi = 1.0
        self.low_date = self.high_date = start_date

def find_best_return(ticks, start_date):
    low = high = 1.0
    low_date = high_date = start_date

    best = BestReturn(start_date)

    current = 1.0
    for (movement, date) in ticks:
        change = 1+(movement*0.01)
        current *= change

        if current < low:
            # better price, not necessarily better roi
            low = high = current
            low_date = high_date = date

        if current == low:
            # same best price, but later date (better return over time)
            low_date = date

        if high < current:
            # better high price
            high = current
            new_roi = high / low
            if new_roi > best.roi:
                # better roi, save it
                best.roi = new_roi
                best.low_date = low_date
                best.high_date = date

    return best
