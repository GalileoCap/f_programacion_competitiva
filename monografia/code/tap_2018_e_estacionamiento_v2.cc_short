//...
#define MAX_N (2 * MAX_M+1)

//...
std::vector<std::vector<std::vector<tfloat>>> Memory(MAX_N, std::vector<std::vector<tfloat>>(MAX_N, std::vector<tfloat>(2, INF)));

//...

tfloat& getAt(tint l, tint r, Direction direction) {
  return Memory[l][r][direction];
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
//...
