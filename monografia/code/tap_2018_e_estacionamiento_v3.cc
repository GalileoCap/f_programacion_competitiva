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
#define MAX_N (2 * MAX_M+1)
#define INF std::numeric_limits<tfloat>::max()

enum Direction {
  LEFT = 0, RIGHT = 1
};

tint N;
std::vector<tfloat> PrefixOdds;
std::vector<std::vector<std::vector<tfloat>>> Memory(MAX_N, std::vector<std::vector<tfloat>>(MAX_N, std::vector<tfloat>(2, INF)));

tfloat& getAt(tint l, tint r, Direction direction) {
  return Memory[l][r][direction];
}

tfloat p(tint l, tint r) { // Probabilidad de que no este en [l, r]
  return 1 - (PrefixOdds[r+1] - PrefixOdds[l]);
}

tfloat f(tint l, tint r, Direction direction) {
  if (l < 0 or r >= N)
    return INF;

  if (l == 0 and r == N-1)
    return 0;

  tfloat& res = getAt(l, r, direction);
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
  std::vector<tfloat> odds(N, 0);
  forn(i, M) std::cin >> odds[i];
  forsn(i, M+1, N) std::cin >> odds[i];

  PrefixOdds.resize(N+1, 0);
  forn(i, N) PrefixOdds[i+1] = PrefixOdds[i] + odds[i];

  // Calculo el resultado
  tfloat res = f(M, M, LEFT);

  // Devuelvo el resultado
  std::cout << FIXED << res << std::endl;
}
