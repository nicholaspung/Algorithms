#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

def eating_cookies(n, cache=None):
  if cache == None:
    cache = [0 for i in range(n+1)]
  if n < 0:
    return 0
  if n == 1 or n == 0:
    return 1
  elif n == 2:
    return 2
  elif cache and cache[n] > 0:
    return cache[n]
  else:
    if not cache or cache[n] == 0:
      cache[n] = eating_cookies(n-3, cache) + eating_cookies(n-2, cache) + eating_cookies(n-1, cache)
    return cache[n]

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')