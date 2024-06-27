from scipy import stats
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# a = 1
# a = 5
a = 15
poissonDist = stats.poisson(a)
x = np.arange(0, 16)
y = poissonDist.pmf(x)

sns.barplot(x = x, y = y, width = 0.1)

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(f"Poisson({a})")
plt.show()