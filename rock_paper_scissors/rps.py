#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  if n == 0:
    return [[]]
  elif n == 1:
    return [['rock'], ['paper'], ['scissors']]
  else:
    rps_under = rock_paper_scissors(n-1)
    base_case = [['rock'], ['paper'], ['scissors']]
    result = []
    for i in range(len(rps_under)):
      a = rps_under[i] + base_case[0]
      b = rps_under[i] + base_case[1]
      c = rps_under[i] + base_case[2]
      result.append(a)
      result.append(b)
      result.append(c)
    return result


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
