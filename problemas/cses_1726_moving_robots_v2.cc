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

#define FIXED std::fixed << std::setprecision(6)

#define MAX_K 100
#define BSZ 8
#define BSZZ (BSZ * BSZ)

tint K;
tfloat arr[MAX_K+1][BSZZ][BSZZ] = {0};

void init() {
  // Inicializa a cada robot en su lugar
  forn(r, BSZZ)
    arr[0][r][r] = 1;
} 

tint arrPos(tint x, tint y) {
  return x + y * BSZ;
}

tfloat dir(tfloat prev[BSZZ], tint x, tint y) {
  return prev[arrPos(x, y)] / ((x-1 >= 0) + (x+1 < BSZ) + (y-1 >= 0) + (y+1 < BSZ));
}

void stepRobot(tfloat prev[BSZZ], tfloat curr[BSZZ]) {
  // Para cada posición, calculo la probabilidad de que se mueva a ella
  fforn(x, y, BSZ) {
    tfloat p = 0;

    if (x-1 >= 0)
      p += dir(prev, x-1, y);
    if (x+1 < BSZ)
      p += dir(prev, x+1, y);

    if (y-1 >= 0)
      p += dir(prev, x, y-1);
    if (y+1 < BSZ)
      p += dir(prev, x, y+1);

    curr[arrPos(x, y)] = p;
  }
}

void step(tfloat prev[BSZZ][BSZZ], tfloat curr[BSZZ][BSZZ]) {
  // Muevo cada robot
  forn(r, BSZZ)
    stepRobot(prev[r], curr[r]);
}

tfloat calcRes() {
  tfloat res = 0;

  // Para cada posición calculo la probabilidad de que no haya ningún robot en ella
  forn(pos, BSZZ) {
    tfloat pC = 1;
    forn(r, BSZZ)
      pC *= (1 - arr[K][r][pos]);
    res += pC;
  }

  return res;
}

tfloat f() {
  init();

  forn(i, K)
    step(arr[i], arr[i+1]);

  return calcRes();
}

void submitRun(void) {
  // Optimizaciones genéricas
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);

  // Recibo la cantidad de pasos a simular
  std::cin >> K;

  // Calculo el resultado
  tfloat res = f();

  // Devuelvo el resultado
  std::cout << FIXED << res << std::endl;
}

void testRun(void) {
  while (true) {
    // Recibo la cantidad de pasos a simular
    if (not (std::cin >> K))
      break;

    tfloat expected;
    std::cin >> expected;
    
    // Calculo el resultado
    tfloat res = f();

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
