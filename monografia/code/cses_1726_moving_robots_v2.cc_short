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
