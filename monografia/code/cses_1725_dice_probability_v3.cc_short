// ...
// Valores máximos dados por la consigna
#define MAX_N 100
#define MAX_B (6 * MAX_N)

std::vector<std::vector<tfloat>> Memory(MAX_N, std::vector<tfloat>(MAX_B, -1)); // Memoria usada para DP, tomo -1 como un valor no establecido

tfloat& getAt(tint j, tint x) {
  return Memory[j-1][x-1];
}

tfloat f(tint j, tint x) { // f(j, x) = P(S_j = x)
  if (not (j <= x and x <= 6 * j)) // Sólo puede dar un resultado entre j y 6j
    return 0.0;

  if (j == 1) // Caso base, un dado sólo
    return 1.0 / 6.0;

  if (getAt(j, x) < 0) { // No fue memoizado
    // f(j, x) = (f(j-1, x-1) + f(j-1), x-2 + ... + f(j-1, x-6))/6
    tfloat res = 0.0;
    for (int i = 1; i <= 6; i++)
      res += f(j - 1, x - i); 
    getAt(j, x) = res / 6.0;
  }

  return getAt(j, x);
}
// ...
