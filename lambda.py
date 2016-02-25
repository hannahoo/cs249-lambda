import re

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

def load_data(path):
  with open(path) as fp:
    temp = fp.readline().strip().split(",") # to ignore the header but to count the number of fields
    num_of_fields = len(temp)
    logger.info("Number of fields: {0}".format(num_of_fields))

    for i in range(0, 5):
      fields = fp.readline().strip().split(",")

      if (len(fields)==num_of_fields):
        newItem = Item()
        newItem.load_from_fields(fields)
        print(newItem)
      else:
        logger.warning("Mismatching fields: {0}".format(fields))


def main():
  #benchmark_data = load_benchmark("benchmark/randomBenchmark.csv")
  load_data("data/train.csv")

if (__name__ == "__main__"):
  main()
