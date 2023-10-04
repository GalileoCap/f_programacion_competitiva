import numpy as np
import itertools as itt

def colPos(x, y, sz):
  return x + sz * y

def genMatrix(sz):
  mat = np.zeros((sz**2, sz**2))

  def getAmnt(x, y):
    if x in [0, sz-1] and y in [0, sz-1]: # On a corner
      return 1/2
    elif x in [0, sz-1] or y in [0, sz-1]: # On a side (not corner)
      return 1/3
    else: return 1/4

  for i, (y, x) in enumerate(itt.product(range(sz), range(sz))):
    amnt = getAmnt(x, y)

    if x != 0:
      mat[colPos(x-1, y, sz), i] = amnt
    if x != sz-1:
      mat[colPos(x+1, y, sz), i] = amnt

    if y != 0:
      mat[colPos(x, y-1, sz), i] = amnt
    if y != sz-1:
      mat[colPos(x, y+1, sz), i] = amnt

  return mat

def matrixAfter(k, sz = 8):
  return np.linalg.matrix_power(genMatrix(sz), k)

def simulate(k, i, sz = 8):
  mat = matrixAfter(k, sz)
  startingArr = np.zeros(sz**2)
  startingArr[i] = 1
  return mat @ startingArr

def solve(k, sz = 8):
  odds = [simulate(k, i, sz) for i in range(sz**2)]

  res = 0
  for (y, x) in itt.product(range(sz), range(sz)):
    foo = 1
    for i in range(sz**2):
      foo *= 1 - odds[i][colPos(x, y, sz)]
    res += foo

  return res

def cses():
  k = int(input())
  res = solve(k, 8)
  print(f'{res:.6f}')
  
def test():
  try:
    while True:
      k = int(input())
      if k == -1:
        break

      expected = float(input())
      res = solve(k)
      print(f'{expected:.6f}, {res:.6f}')
  except EOFError:
    return

if __name__ == '__main__':
  cses()
  # test()
