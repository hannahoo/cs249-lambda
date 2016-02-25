import re

def load_benchmark(path, excludeHeader=True):
  ret = {}
  with open(path) as fp:
    if (excludeHeader):
      temp = fp.readline()      
    
    for line in fp:
      fields = line.strip().split(",")
           
      if (not(fields[0] in ret)):
        ret[fields[0]] = []
        
      ret[fields[0]].append(fields[1])
  return ret

def main():
  benchmark_data = load_benchmark("../randomBenchmark.csv")
  print(len(benchmark_data))

  
if (__name__ == "__main__"):
  main()


