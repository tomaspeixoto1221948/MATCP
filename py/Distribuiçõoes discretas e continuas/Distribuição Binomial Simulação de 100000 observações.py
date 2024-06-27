from scipy import stats
import matplotlib.pyplot as plt

# Simulacao de 100000 observacoes de uma distribuicao Binomial,
# Bi(n = 40, p = 0.5).

(p, num) = (0.5, 40)
binomDist = stats.binom(num, p)
n = 100000

trials = binomDist.rvs(n)

plt.hist(trials, bins = 'auto')
plt.show()


