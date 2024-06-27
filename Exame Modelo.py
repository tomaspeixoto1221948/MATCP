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

p7 = stats.binom.pmf(36, 55, p6)
print(f'{p7:.4f}')

# P3

beta = -0.7 / np.log(0.11)

p8 = 1 - stats.gamma.cdf(1.5, a = 1, scale = beta)
p9 = 1 - stats.gamma.cdf(2.3, a = 1, scale = beta)
print(f'{p9 / p8:.4f}')

p10 = stats.gamma.ppf(0.5, a = 1, scale = beta)
print(f'{p10:.4f}')

# P4

p11 = stats.norm.cdf(300, 295, 14)
print(f'{p11:.4f}')

p12 = stats.norm.cdf(0, 330 - 295, np.sqrt(9**2 + 14**2))
print(f'{p12:.4f}')

mu = 5 * 330 + 5 * 295 + 550
sigma = (5 * 9**2) + (5 * 14**2)
print(f'{mu:.4f}')
print(f'{sigma:.4f}')

p13 = stats.norm.cdf(3700, mu, np.sqrt(sigma))
print(f'{p13:.4f}')

p14 = stats.binom.cdf(6, 12, 1 - p13)
print(f'{p14:.4f}')

p15 = stats.binom.pmf(4, 12, 1 - p13)
print(f'{p15:.4f}')

