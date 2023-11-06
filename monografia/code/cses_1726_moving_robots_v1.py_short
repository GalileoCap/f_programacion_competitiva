import numpy as np
import itertools as itt

def colPos(x, y, sz):
  return x + sz * y

def genMatrix(sz): # Genera la matriz de transición para un tablero de lado sz
  mat = np.zeros((sz**2, sz**2))

  def getAmnt(x, y):
    if x in [0, sz-1] and y in [0, sz-1]: # En una esquina
      return 1/2
    elif x in [0, sz-1] or y in [0, sz-1]: # En un costado (y no una esquina)
      return 1/3
    else: return 1/4

  for i, (y, x) in enumerate(itt.product(range(sz), range(sz))):
    amnt = getAmnt(x, y)

    if x-1 >= 0:
      mat[colPos(x-1, y, sz), i] = amnt
    if x+1 < sz:
      mat[colPos(x+1, y, sz), i] = amnt

    if y-1 >= 0:
      mat[colPos(x, y-1, sz), i] = amnt
    if y+1 < sz-1:
      mat[colPos(x, y+1, sz), i] = amnt

  return mat

def matrixAfter(k, sz = 8):
  return np.linalg.matrix_power(genMatrix(sz), k)

def simulate(k, i, sz = 8):
  mat = matrixAfter(k, sz)
  v0 = np.zeros(sz**2)
  v0[i] = 1
  return mat @ v0

def solve(k, sz = 8):
  odds = [simulate(k, r, sz) for r in range(sz**2)]

  res = 0
  for (y, x) in itt.product(range(sz), range(sz)):
    foo = 1
    for i in range(sz**2):
      foo *= 1 - odds[i][colPos(x, y, sz)]
    res += foo

  return res
