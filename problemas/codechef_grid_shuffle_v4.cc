#include <ios>
#include <iostream>
#include <iomanip>
#include <limits>

using tint = long long;
using tfloat = long double;

#define forsn(i, s, n) for (tint i = s; i < tint(n); i++)
#define forn(i, n) forsn(i, 0, n)
#define fforsn(i, j, s, n) forsn(i, s, n) forsn(j, s, n)
#define fforn(i, j, n) fforsn(i, j, 0, n)

#define MAX_T 5
#define MAX_N 1000
#define MAX_K MAX_N
#define MOD 998244353

tint T, N, K, R, C;
tint M[4][4];
tint V[MAX_T][MAX_K+1][4] = {0};

tint gcdExtended(tint a, tint b, tint *x, tint *y){
  if (a == 0) { // Caso base
    *x = 0; *y = 1;
    return b;
  }

  tint x1, y1; // Para almacenar los resultados de las llamadas recursivas
  tint gcd = gcdExtended(b%a, a, &x1, &y1);

  // Actualiza x e y usando los resultados de la llamada recursiva recursive call
  *x = y1 - (b/a) * x1;
  *y = x1;

  return gcd;
}

tint inverseMod(tint a) {
  tint x, y;
  gcdExtended(a, MOD, &x, &y);
  return x;
}

void calcMatrix(tint n) {
  tint gamma = inverseMod(2 * n * n),
       beta = ((n-1) * gamma) % MOD, 
       alpha = (1 - 2 * beta) % MOD,
       delta = (1 - (gamma + beta)) % MOD,
       epsilon = (1 - 2 * gamma);

  M[0][0] = alpha; M[0][1] = beta; M[0][2] = beta; M[0][3] = 0;
  M[1][0] = gamma; M[1][1] = delta; M[1][2] = 0; M[1][3] = beta;
  M[2][0] = gamma; M[2][1] = 0; M[2][2] = delta; M[2][3] = beta;
  M[3][0] = 0; M[3][1] = gamma; M[3][2] = gamma; M[3][3] = epsilon;
}

void step(tint prev[4], tint curr[4]) {
  fforn(i, j, 4)
    curr[i] += (M[j][i] * prev[j]) % MOD;

  forn(i, 4)
    curr[i] %= MOD;
}

int main(void) {
  // Optimizaciones genéricas
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  std::cout.tie(nullptr);

  std::cin >> T;
  forn(_r, T) {
    // Recibo el input
    std::cin >> N >> K >> R >> C;

#ifdef TEST
    tint expected;
    std::cin >> expected;
#endif // TEST

    // Calculo su matriz de transición
    calcMatrix(N);

    // Preparo al vector inicial
    V[_r][0][0] = 1;

    // Simulo k pasos
    forn(i, K)
      step(V[_r][i], V[_r][i+1]);

    // Obtengo el resultado
    tint res = V[_r][K][0];

    // Devuelvo el resultado
#ifdef TEST
    std::cout << expected << ' ' << res << std::endl;
#else
    std::cout << res << std::endl;
#endif // TEST
  }
}
