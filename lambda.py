import re
import os

import logging
logger = logging.getLogger('lambda')
logging.basicConfig(filename='lambda.log', level=logging.DEBUG)

import coloredlogs
coloredlogs.install(level='DEBUG')

import numpy as np
from scipy.stats import itemfreq

from item import Item

class GlobalData(object):
    _name = None
    _internal = {}

    def __init__(self, name):
        self._name = name
        self._internal = {  "srch_id": {"type": np.integer, "data": None},
                            "date_time": {"type": np.chararray, "data": None},
                            "price_usd": {"type": np.float, "data": None},
                            "site_id": {"type": np.integer, "data": None},
                            "visitor_hist_starrating": {"type": np.float, "data": None},
                            "visitor_hist_adr_usd": {"type": np.float, "data": None},
                            "prop_country_id": {"type": np.integer, "data": None},
                            "prop_id": {"type": np.integer, "data": None},
                            "prop_starrating": {"type": np.integer, "data": None},
                            "prop_review_score": {"type": np.float, "data": None},
                            "prop_brand_bool": {"type": np.integer, "data": None},
                            "prop_location_score1": {"type": np.float, "data": None},
                            "prop_location_score2": {"type": np.float, "data": None},
                            "prop_log_historical_price": {"type": np.float, "data": None},
                            }

    def load(self, attribute):
        np_array = np.load(self.get_path(attribute))
        self._internal[attribute]["data"] = np_array
        logger.info("Attribute ({0}) {1} items are loaded.".format(attribute, np_array.size))

    def get(self, attribute):
        return self._internal[attribute]["data"]

    def convert(self, attribute, raw_array, auto_save):
        logger.info("Converting the attribute ({0})...".format(attribute))
        np_array = np.array(raw_array).astype(self._internal[attribute]["type"])
        self._internal[attribute]["data"] = np_array
        if auto_save:
            np.save(self.get_path(attribute), np_array)
        logger.info("Attribute ({0}) {1} items are converted.".format(attribute, np_array.size))

    def save(self, attribute):
        np_array = self._internal[attribute]["data"]
        np.save(self.get_path(attribute), np_array)
        logger.info("Attribute ({0}) {1} items are saved.".format(attribute, np_array.size))

    def get_path(self, attribute):
        return "data_numpy/{0}_{1}.npy".format(self._name, attribute)

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

def load_data(path, action):
    pass

def convert_data_to_numpy(path, train_data):
    line_number = 0
    with open(path) as fp:
        temp = fp.readline().strip().split(",") # to ignore the header but to count the number of fields
        num_of_fields = len(temp)
        logger.info("Number of fields: {0}".format(num_of_fields))

        need_to_be_convert = ["srch_id", "date_time", "price_usd", "site_id",
            "visitor_hist_starrating", "visitor_hist_adr_usd",
            "prop_country_id", "prop_id", "prop_starrating", "prop_review_score",
            "prop_brand_bool", "prop_location_score1", "prop_location_score2", "prop_log_historical_price"]
        temp_array = {}
        for key in need_to_be_convert:
            temp_array[key] = []

        for i in range(0,10000): # partial convertion
            linebuf = fp.readline()
        #for linebuf in fp: # full convertion
            line_number = line_number + 1
            fields = linebuf.strip().split(",")

            if (line_number % 1000 == 0 ):
                print "Reading the line : {0}\r".format(line_number),

            if (len(fields)==num_of_fields):
                new_item = Item()
                new_item.load_from_fields(fields)

                for key in temp_array.keys():
                    temp_array[key].append(new_item[key])
            else:
                logger.warning("Mismatching fields: {0}".format(fields))

        print ""

        # Already done! "False" wouldn't save the numpy array again.
        #train_data.convert("srch_id", array_srch_id, False)
        #train_data.convert("date_time", array_date_time, False)
        #train_data.convert("price_usd", array_price_usd, False)
        #train_data.convert("site_id", array_site_id, False)



        for key in need_to_be_convert:
            train_data.convert(key, temp_array[key], True)

        logger.info("Completed: {0}".format(line_number))

def main():
    #convert_data_to_numpy("data/train.csv")
    train_data = GlobalData("train")
    convert_data_to_numpy("data/train.csv", train_data)

    train_data = GlobalData("train")
    train_data.load("prop_log_historical_price")
    np_array = train_data.get("prop_log_historical_price")
    print(itemfreq(np_array))

if __name__ == "__main__":
    main()
