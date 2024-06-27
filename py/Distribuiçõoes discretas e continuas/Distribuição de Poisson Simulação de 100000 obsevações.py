from scipy import stats
import matplotlib.pyplot as plt

# Simulacao de 100000 observacoes de uma distribuicao de Poisson,
# Poisson (λ = 20).

lambd = 20
poissonDist = stats.poisson(lambd)
n = 100000

trials = poissonDist.rvs(n)

plt.hist(trials, bins = 'auto')
plt.show()