import re
import os

import logging
logger = logging.getLogger('lambda')
logging.basicConfig(filename='lambda.log', level=logging.DEBUG)

import coloredlogs
coloredlogs.install(level='DEBUG')

from item import Item

def load_benchmark(path):
    ret = {}
    with open(path) as fp:
        temp = fp.readline() # to ignore the header

    for line in fp:
        fields = line.strip().split(",")

        if (not(fields[0] in ret)):
            ret[fields[0]] = []

        ret[fields[0]].append(fields[1])

    logger.info("Number of benchmark items: %d".format(len(ret)))
    return ret

#category = {}
#category["site_id"] = {}
#category["booking_bool"] = {}
##category["gross_bookings_usd"] = {}
#category["click_bool"] = {}
#category["comp1_rate"] = {}
#category["comp1_inv"] = {}
#category["comp1_rate_percent_diff"] = {}
#
#category["price_usd"] = {}
#
#category["prop_location_score1"] = {}
#category["prop_location_score2"] = {}
#
#def add_count(category_name, data):
#    if not(data in category[category_name]):
#        category[category_name][data] = 0
#    category[category_name][data] = category[category_name][data] + 1

def load_data(path, action):
    num_of_items = 0
    with open(path) as fp:
        temp = fp.readline().strip().split(",") # to ignore the header but to count the number of fields
        num_of_fields = len(temp)
        logger.info("Number of fields: {0}".format(num_of_fields))

        action.initialize()

        for linebuf in fp:
            fields = linebuf.strip().split(",")

            if (len(fields)==num_of_fields):
                newItem = Item()
                newItem.load_from_fields(fields)
                action.provide_item( newItem )
            else:
                logger.warning("Mismatching fields: {0}".format(fields))

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

    def provide_item(self, newItem):
        price = float(newItem.price_usd)
        self.stat_count = self.stat_count + 1

        if (self.stat_count % 10000 == 0):
            print "Count: {0}, Min: {1}, Max: {2}, Min_Pos: {3}, Max_Pos : {4}\r".format(self.stat_count, self.min_value, self.max_value, self.min_pos, self.max_pos),

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


def main():
    normalize_price = NormalizePrice()
    load_data("data/train.csv", normalize_price)
    print("========")
    print(normalize_price.min_value)
    print(normalize_price.max_value)
    print(normalize_price.min_pos)
    print(normalize_price.max_pos)
    print(normalize_price.stat_count)

if __name__ == "__main__":
    main()
