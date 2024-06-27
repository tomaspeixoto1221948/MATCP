import scipy.integrate as integrate
from scipy import stats
import numpy as np

#
result = integrate.quad(lambda x: x**2, 0, 1)
print(f'{result[0]:.3}')