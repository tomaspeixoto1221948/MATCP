from scipy import stats
import matplotlib.pyplot as plt

(p, num) = (0.5, 40)
binomDist = stats.binom(num, p)

n = 100000
trials = binomDist.rvs(n)
plt.hist(trials, bins = 'auto')
plt.show()


