from scipy import stats
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

#(p, num) = (0.1, 5)
#(p, num) = (0.1, 10)
#(p, num) = (0.5, 5)
(p, num) = (0.1, 5)
binomDist = stats.binom(num, p)

# Generate 5 numeros inteiros sequencias
x = np.arange(0, 6)
y = binomDist.pmf(x)

sns.barplot(x=x, y=y, width=0.1)

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(f"Bin({num}, {p})")
plt.show()


