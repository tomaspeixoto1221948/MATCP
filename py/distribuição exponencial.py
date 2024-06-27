import scipy.integrate as integrate
from scipy import stats
import numpy as np

# F(X) = 1 - e^(-x/Beta)
# F(X < 0.7) = 0.89
# 1 - e^(-0.7 / Beta) = 0.89
# e^(-0.7 / Beta) = 0.11
# -0.7 / Beta = ln(0.11)
# Beta = -0.7 / ln(0.11)

beta = -0.7 / np.log(0.11)
print(f'P3(1.) Beta = {beta:.4f}')

# P (X > 1.5) = 1 - P(X ≤ 1.5)
p8 = 1 - stats.gamma.cdf(1.5, a = 1, scale = beta)
print(f'A probabilidade é {p8:.4f}')

# P (X > 2.3) / P (X > 1.5)
p9 = 1 - stats.gamma.cdf(2.3, a = 1, scale = beta)
p10 = 1 - stats.gamma.cdf(1.5, a = 1, scale = beta)
print(f'P3(2.) A probabilidade é {p9 / p10:.4f}')

# P (X > q) = 0.5
q = stats.gamma.ppf(0.5, a = 1, scale = beta)
print(f'P3(3.) q={q:.4f}')