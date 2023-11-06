// ...
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

tfloat P(tint j, tint a, tint b) { // P(a <= S_j <= b)
  tfloat res = 0.0; // P(a <= S_j <= b) = P(S_j = a) + P(S_j = a+1) + ... + P(S_j = b)
  for (int i = a; i <= b; i++)
    res += f(j, i);
  return res;
}
// ...
