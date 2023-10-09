// Time Limit Exceded

#include <ios>
#include <iostream>
#include <iomanip>

using tint = int;
using tfloat = float;

tfloat f(tint j, tint x) { // f(j, x) = P(S_j = x)
  if (not (j <= x and x <= 6*j))
    return 0;

  if (j == 1) // Caso base, un sólo dado
    return 1.0 / 6.0;
  
  tfloat res = 0.0; // f(j, x) = (f(j-1, x-1) + f(j-1), x-2 + ... + f(j-1, x-6))/6
  for (int i = 1; i <= 6; i++)
    res += f(j - 1, x - i); 

  return res / 6.0;
}

int main(void) {
  // Optimizaciones genéricas
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  std::cout.tie(nullptr);

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
