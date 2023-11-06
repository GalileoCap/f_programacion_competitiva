// ...
enum Direction {
  LEFT, RIGHT
};

tint N;
std::vector<tfloat> Odds;

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

  tfloat pC = p(l, r);
  tint distance = r - l + 1; // Distancia a caminar si cambio de dirección
  tfloat mantenerDir = pC + (direction == LEFT ? f(l-1, r, LEFT) : f(l, r+1, RIGHT)),
         cambiarDir = pC * (r - l + 1) + (direction == LEFT ? f(l, r+1, RIGHT) : f(l-1, r, LEFT));

  return std::min(mantenerDir, cambiarDir);
}
//...
