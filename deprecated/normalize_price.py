class NormalizePrice(object):
    min_value = None
    max_value = None
    stat_count = 0

    def initialize(self):
        self.min_value = None
        self.min_pos = None
        self.max_value = None
        self.max_pos = None
        self.stat_count = 0

    def provide_item(self, newItem, raw):
        price = float(newItem.price_usd)
        self.stat_count = self.stat_count + 1

        if (self.min_value is None):
            self.min_value = price
        else:
            if (price < self.min_value):
                self.min_value = price
                self.min_pos = self.stat_count

        if (self.max_value is None):
            self.max_value = price
        else:
            if (price > self.max_value):
                self.max_value = price
                self.max_pos = self.stat_count
                print(newItem)
                print(raw)
