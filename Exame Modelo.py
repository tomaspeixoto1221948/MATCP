import scipy.integrate as integrate
from scipy import stats
import numpy as np

# P1
result_1 = integrate.quad(lambda x: x**0.2 * np.exp(-x**0.2), 1, 1.4)
valor_lambda = 1 / result_1[0]
print(f'{valor_lambda:.2}')

result_2 = integrate.quad(lambda x: valor_lambda * x**0.2 * np.exp(-x**0.2), 1, 1.2)
print(f'{result_2[0]:.2}')

result_3 = integrate.quad(lambda x: valor_lambda * x**0.2 * np.exp(-x**0.2), 1, 1.3)
print(f'{result_3[0]:.2}')

result_4 = integrate.quad(lambda x: valor_lambda * x**0.2 * np.exp(-x**0.2), 1.35, 1.4)
print(f'{result_4[0]:.2}')

result_5 = integrate.quad(lambda x: x * valor_lambda * x**0.2 * np.exp(-x**0.2), 1, 1.4)
print(f'{result_5[0]:.3}')

# P2
p1 = 1 - stats.poisson.cdf(6, 4.4)
print(f'{p1:.4}')

p2 = stats.poisson.cdf(11, 4 * 5.4)
print(f'{p2:.2}')

p3 = stats.poisson.cdf(14, 4.4 + 5.4) - stats.poisson.cdf(10, 4.4 + 5.4)
print(f'{p3:.2}')

p4 = stats.norm.cdf(15,12,4) - stats.norm.cdf(10,12,4)
print(f'{p4:.4f}')

p5 = stats.norm.cdf(15, 12, np.sqrt(16 / 10)) - stats.norm.cdf(10, 12, np.sqrt(16 / 10))
print(f'{p5:.4f}')

p6 = stats.norm.cdf(15, 12, 4)
p6_binom = stats.binom.pmf(36, 55, p6)
print(f'{p6_binom:.4f}')