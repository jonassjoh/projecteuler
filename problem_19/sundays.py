class Date:

    months = [
        31,         # Jan
        [28, 29],   # Feb
        31,         # Mar
        30,         # Apr
        31,         # May
        30,         # Jun
        31,         # Jul
        31,         # Aug
        30,         # Sep
        31,         # Okt
        30,         # Nov
        31          # Dec
    ]

    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y
        self._d = 0

    def next(self):
        self.d += 1
        self._d += 1
        md = self.month_days(self.m, self.y)
        if self.d >= md:
            self.d = 0
            self.m += 1
            if self.m >= 12:
                self.m = 0
                self.y += 1

    def weekday(self, d):
        return d % 7

    def month_days(self, m, y):
        if m == 1:
            return self.months[m][0] if self.leap_year(y) else self.months[m][1]
        return self.months[m]

    def leap_year(self, y):
        if y % 100 and y % 400:
            return True
        return y % 4

date = Date(1, 0, 1901)
s = 0
while date.y < 2001:
    if date.d == 0 and date.weekday(date._d) == 6:
        s += 1
    date.next()

print(s)
