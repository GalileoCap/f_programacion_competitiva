// 1029ms, 188900KB

#include <ios>
#include <iostream>
#include <iomanip>
#include <limits>
#include <tuple>
#include <vector>
#include <map>

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
std::vector<tfloat> PrefixOdds;

using Case = std::tuple<tint, tint, Direction>;
std::map<Case, tfloat> Memory;

tfloat f(tint l, tint r, Direction direction) {
  if (l < 0 or r >= N)
    return INF;

  if (l == 0 and r == N-1)
    return 0;

  const Case thisCase = {l, r, direction};
  if (Memory.count(thisCase) == 0) {
    tfloat pC = 1 - (PrefixOdds[r+1] - PrefixOdds[l]); // Probabilidad de que NO esté en este rango
    tint distance = r - l + 1; // Distancia a caminar si cambio de dirección
    tfloat goingLeft = pC * (direction == RIGHT ? distance : 1) + f(l - 1, r, LEFT),
           goingRight = pC * (direction == LEFT ? distance : 1) + f(l, r + 1, RIGHT);

    Memory[thisCase] = std::min(goingLeft, goingRight);
#ifdef VERBOSE
    std::cout << "f(" << l << ", " << r << ", " << (direction == LEFT ? "L" : "R") << ") = " << FIXED << Memory[thisCase] << std::endl;
#endif
  }

  return Memory[thisCase];
}

void submitRun(void) {
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

  // Calculo el vector de prefijos
  PrefixOdds.resize(N+1, 0);
  forn(i, N) PrefixOdds[i+1] = PrefixOdds[i] + odds[i];

  // Calculo el resultado
  tfloat res = f(M, M, LEFT);

  // Devuelvo el resultado
  std::cout << FIXED << res << std::endl;
}

void testRun(void) {
  while (true) {
    // Limpio la memoria
    Memory.clear();

    // Recibo la cantidad de calles a cada lado
    tint M;
    if (not (std::cin >> M))
      break;
    N = 2*M+1;

    // Recibo las probabilidades por calle
    std::vector<tfloat> odds(N, 0);
    forn(i, M) std::cin >> odds[i];
    forsn(i, M+1, N) std::cin >> odds[i];

    // Calculo el vector de prefijos
    PrefixOdds.resize(N+1, 0);
    forn(i, N) PrefixOdds[i+1] = PrefixOdds[i] + odds[i];

    tfloat expected;
    std::cin >> expected;
    
    // Calculo el resultado
    tfloat res = f(M, M, LEFT);

    // Devuelvo el resultado
    std::cout << FIXED << expected << " " << res << std::endl;
  }
}

int main(void) {
#ifndef TEST
  submitRun();
#else
  testRun();
#endif
}
