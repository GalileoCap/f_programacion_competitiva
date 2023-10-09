import numpy as np
import itertools as itt

MOD = 998_244_353

def inverseMod(x):
  return pow(x, -1, MOD)

def inputLine():
  n, k, r, c = [int(x) for x in input().split()]
  return n, k, r-1, c-1

def colPos(x, y, sz):
  return x + sz * y

def genMatrix(sz):
  # mat = np.zeros((4, 4))
  # beta = 1/2 * 1/sz * (sz-1)/sz # r+, c+ -> r+, c- = elije rotar fila y elije rotar esta fila y no le pega al lugar correcto [Similar para r+, c+ -> r-, c+ y r+, c- -> r-, c- y r-, c+ -> r-, c-]
  # alpha = 1 - 2 * beta
  # gamma = 1/2 * 1/sz * 1 / sz # r+, c- -> r+, c+ = elije rotar fila y elije rotar esta fila y le pega al lugar correct [Similar para r-, c+ -> r+, c+ y r-, c- -> r+, c- y r-, c- -> r-, c+]
  # delta = 1 - (gamma + beta)
  # epsilon = 1 - 2 * gamma

  # alpha = 1/2 * (1/sz * 1/sz + (sz-1)/sz) + 1/2 * (1/sz * 1/sz + (sz-1)/sz) # r+, c+ -> r+, c+ = (elije rotar fila y ((elije rotar esta fila y le pega al lugar correcto) o elije rotar otra fila)) o (elije rotar columna y ((elije rotar esta columna y le pega al lugar correcto) o elije rotar otra columna))
  # beta = 1/2 * 1/sz * (sz-1)/sz # r+, c+ -> r+, c- = elije rotar fila y elije rotar esta fila y no le pega al lugar correcto [Similar para r+, c+ -> r-, c+ y r+, c- -> r-, c- y r-, c+ -> r-, c-]
  # gamma = 1/2 * 1/sz * 1 / sz # r+, c- -> r+, c+ = elije rotar fila y elije rotar esta fila y le pega al lugar correct [Similar para r-, c+ -> r+, c+ y r-, c- -> r+, c- y r-, c- -> r-, c+]
  # delta = 1/2 * (1/sz * (sz-1)/sz + (sz-1)/sz) + 1/2 * (sz-1)/sz # r+, c- -> r+, c- = (elije rotar fila y ((elije rotar esta fila y no le pega al lugar correcto) o elije rotar otra fila)) o (elije rotar columna y no elije rotar esta columna) [Similar para r-, c+ -> r-, c+]
  # epsilon = 1/2 * (1/sz * (sz-1)/sz + (sz-1)/sz) + 1/2 * (1/sz * (sz-1)/sz + (sz-1)/sz) # r-, c- -> r-, c- = (elije rotar fila y ((elije rotar esta fila y no le pega al lugar correcto) o elije rotar tora fila)) o (elije rotar columna y ((elije rotar esta columna y no le pega al lugar correcto) o elije rotar otra columna))

  mat = np.zeros((4, 4), dtype = np.int64)
  beta = (sz-1) * inverseMod(2 * sz**2) % MOD # r+, c+ -> r+, c- = elije rotar fila y elije rotar esta fila y no le pega al lugar correcto [Similar para r+, c+ -> r-, c+ y r+, c- -> r-, c- y r-, c+ -> r-, c-]
  alpha = (1 - 2 * beta) % MOD
  gamma = inverseMod(2 * sz**2) # r+, c- -> r+, c+ = elije rotar fila y elije rotar esta fila y le pega al lugar correct [Similar para r-, c+ -> r+, c+ y r-, c- -> r+, c- y r-, c- -> r-, c+]
  delta = (1 - (gamma + beta)) % MOD
  epsilon = (1 - 2 * gamma) % MOD

  return np.transpose(np.array([
    [alpha, beta, beta, 0],
    [gamma, delta, 0, beta],
    [gamma, 0, delta, beta],
    [0, gamma, gamma, epsilon],
  ]))

  return mat

def simulate(k, sz):
  mat = genMatrix(sz)
  # arr = np.zeros(4)
  arr = np.zeros(4, dtype = np.int64)
  arr[0] = 1

  for _ in range(k):
    arr = (mat @ arr) % MOD

  return arr

def solve(k, r, c, sz):
  odds = simulate(k, sz)
  return odds[0] % MOD

def codechef():
  for _ in range(int(input)):
    n, k, r, c = inputLine()
    print(solve(k, r, c, n))
  
def test():
  for _ in range(int(input())):
    n, k, r, c = inputLine()
    expected = int(input())
    print(expected, solve(k, r, c, n))

if __name__ == '__main__':
  # np.set_printoptions(precision = 3)
  # codechef()
  test()
