from cses_1726_moving_robots_v1 import solve

def printVect(v):
  print('{', end = '')
  for i in range(len(v)-1):
    print(v[i], ', ', sep = '', end = '')
  print(v[-1], end = '')
  print('}')

if __name__ == '__main__':
  res = [solve(k, 8) for k in range(100 + 1)]
  printVect(res)
