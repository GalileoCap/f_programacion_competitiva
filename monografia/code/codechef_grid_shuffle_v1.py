# 0.08s

MOD = 998_244_353

def inputLine():
  n, k, r, c = [int(x) for x in input().split()]
  return n, k, r-1, c-1

def inverseMod(x):
  return pow(x, -1, MOD)

def genMatrix(sz):
  beta = (sz-1) * inverseMod(2 * sz**2) % MOD # r+, c+ -> r+, c- = elije rotar fila y elije rotar esta fila y no le pega al lugar correcto [Similar para r+, c+ -> r-, c+ y r+, c- -> r-, c- y r-, c+ -> r-, c-]
  alpha = (1 - 2 * beta) % MOD
  gamma = inverseMod(2 * sz**2) # r+, c- -> r+, c+ = elije rotar fila y elije rotar esta fila y le pega al lugar correct [Similar para r-, c+ -> r+, c+ y r-, c- -> r+, c- y r-, c- -> r-, c+]
  delta = (1 - (gamma + beta)) % MOD
  epsilon = (1 - 2 * gamma) % MOD

  print('A', alpha, beta, gamma, delta, epsilon)

  return [
    [alpha, beta, beta, 0],
    [gamma, delta, 0, beta],
    [gamma, 0, delta, beta],
    [0, gamma, gamma, epsilon],
  ]

def vprod(v, w):
  return v[0] * w[0] + v[1] * w[1] + v[2] * w[2] + v[3] * w[3]

def step(mat, v):
  return [vprod(mat[i], v) for i in range(4)]

def simulate(k, sz):
  mat = genMatrix(sz)
  v = [1, 0, 0, 0]

  for _ in range(k):
    v = step(mat, v)

  return v

def solve(k, r, c, sz):
  odds = simulate(k, sz)
  return odds[0] % MOD

if __name__ == '__main__':
  for _ in range(int(input())):
    n, k, r, c = inputLine()
    print(solve(k, r, c, n))
