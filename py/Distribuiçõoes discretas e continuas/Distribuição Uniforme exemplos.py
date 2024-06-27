from scipy import stats

# A probabilidade do numero estar compreendido entre 6.30 e 6.95
# é P(6.30 ≤ X ≤ 6.95).
x = 6.95
y = 6.30
p1 = stats.uniform.cdf(x, 5, 2) - stats.uniform.cdf(y, 5, 2)
print(f'A probabilidade de do numero estar compreendido entre {x} e {y} é {p1:.3f}')

# A probabilidade do numero estar compreendido entre 6.50 e 7.50
# é P(6.50 ≤ X ≤ 7.50).
a = 6.50
b = 7.50
p2 = stats.uniform.cdf(b, 5, 2) - stats.uniform.cdf(a, 5, 2)
print(f'A probabilidade de do numero estar compreendido entre {a} e {b} é {p2:.3f}')

# A probabilidade de ambas serem maiores do que 0.75 ´e
# P(X1 > 0.75 e X2 > 0.75).
z = 0.75
p3 = (1 - stats.uniform.cdf(z, 0, 1)) ** 2
print(f'A probabilidade de ambas serem maiores do que {z} é {p3:.3f}')

