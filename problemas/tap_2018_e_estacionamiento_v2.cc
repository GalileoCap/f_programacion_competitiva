// 498ms, 284900KB

#include <ios>
#include <iostream>
#include <iomanip>
#include <limits>
#include <vector>

using tint = long long;
using tfloat = long double;

#define forsn(i, s, n) for (tint i = s; i < tint(n); i++)
#define forn(i, n) forsn(i, 0, n)

#define FIXED std::fixed << std::setprecision(6)

#define MAX_M 1000
#define INF std::numeric_limits<tfloat>::max()

enum Direction {
  LEFT = 0, RIGHT = 1
};

tint N;
std::vector<tfloat> Odds;
std::vector<std::vector<std::vector<tfloat>>> Memory;

tfloat p(tint l, tint r) { // Probabilidad de que no este en [l, r]
  tfloat res = 0;
  for (tint i = l; i <= r; i++)
    res += Odds[i];
  return 1 - res;
}

tfloat f(tint l, tint r, Direction direction) {
  if (l < 0 or r >= N)
    return INF;

  if (l == 0 and r == N-1)
    return 0;

  tfloat& res = Memory[l][r][direction];
  if (res < INF)
    return res;

  tfloat pC = p(l, r); // Probabilidad de que no esté en este rango
  tint distance = r - l + 1; // Distancia a caminar si cambio de dirección
  tfloat mantenerDir = pC + (direction == LEFT ? f(l-1, r, LEFT) : f(l, r+1, RIGHT)),
         cambiarDir = pC * (r - l + 1) + (direction == LEFT ? f(l, r+1, RIGHT) : f(l-1, r, LEFT));

  return res = std::min(mantenerDir, cambiarDir);
}

int main(void) {
  // Optimizaciones genéricas
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);

  // Recibo la cantidad de calles a cada lado
  tint M;
  std::cin >> M;
  N = 2*M+1;

  // Recibo las probabilidades por calle
  Odds.resize(N);
  forn(i, M) std::cin >> Odds[i];
  forsn(i, M+1, N) std::cin >> Odds[i];

  Memory.resize(N, std::vector<std::vector<tfloat>>(N, std::vector<tfloat>(2, INF)));

  // Calculo el resultado
  tfloat res = f(M, M, LEFT);

  // Devuelvo el resultado
  std::cout << FIXED << res << std::endl;
}
