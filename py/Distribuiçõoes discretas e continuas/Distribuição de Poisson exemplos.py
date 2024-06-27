from scipy import stats

# X10 ∼ Poisson(λ = 1.5)
# X30 ∼ Poisson(3 × λ = 4.5)

# A probabilidade de a associaçao nao receber qualquer chamada
# é P(X10 = 0):
p1 = stats.poisson.pmf(0, 1.5)
print(f'A prob. de não receber qualquer chamada é {p1:.3f}')

# A probabilidade de a associacao receber mais de duas chamadas
# é P(X10 > 2) = 1 − P(X10 ≤ 2):
p2 = 1 - stats.poisson.cdf(2, 1.5)
print(f'A prob. de não receber qualquer chamada é {p2:.3f}')


# A probabilidade de a associacao nao receber qualquer chamada
# é P(X30 = 0):
p3 = stats.poisson.pmf(0, 4.5)
print(f'A prob. de não receber qualquer chamada é {p3:.3f}')

# A probabilidade de aassociacao receber mais de duas chamadas
# é P(X30 > 2) = 1 − P(X30 ≤ 2):
p4 = 1 - stats.poisson.cdf(2, 4.5)
print(f'A prob. de não receber qualquer chamada é {p4:.3f}')
