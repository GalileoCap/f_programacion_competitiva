#include <ios>
#include <iostream>
#include <iomanip>

using tint = int;
using tfloat = float;

tfloat f(tint j, tint x) { // f(j, x) = P(S_j = x)
  if (j == 1) { // Caso base, un sólo dado
    if (1 <= x and x <= 6) // Sólo puede dar un resultado entre 1 y 6
      return 1.0 / 6.0;
    else return 0.0;
  }
  
  tfloat res = 0.0; // f(j, x) = (f(j-1, x-1) + f(j-1), x-2 + ... + f(j-1, x-6))/6
  for (int i = 1; i <= 6; i++)
    res += f(j - 1, x - i); 

  return res / 6.0;
}

void submitRun(void) {
  // Optimizaciones genéricas
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);

  // Recibo el input
  tint n, a, b;
  std::cin >> n >> a >> b;
  
  // Calculo el resultado como P(S = a) + P(S = a+1) + ... + P(S = b)
  tfloat res = 0.0;
  for (int i = a; i <= b; i++)
    res += f(n, i);

  // Devuelvo el resultado
  std::cout << std::fixed << std::setprecision(6) << res << std::endl;
}

void testRun(void) {
  while (not std::cin.eof())
    submitRun();
}

int main(void) {
#ifndef TEST
  submitRun();
#else
  testRun();
#endif
}
