from scipy import stats

# A probabilidade da Sara ganhar exatamente em 10 jogos é
# P(X = 10):
p1 = stats.binom.pmf(10, 15, 0.6)
print(f'A probabilidade de a Sara ganhar é {p1:.3f}')

# A probabilidade da Sara ganhar em pelo menos 10 jogos é
#P(X ≥ 10) = 1 − P(X ≤ 9):
p2 = 1 - stats.binom.cdf(9, 15, 0.6)
print(f'A probabilidade de a Sara ganhar é {p2:.3f}')

# A probabilidade da Sara ganhar entre 4 e 8 jogos é
# P(4 ≤ X ≤ 8) = P(X ≤ 8) − P(X ≤ 3):
p3 = stats.binom.cdf(8, 15, 0.6) - stats.binom.cdf(3, 15, 0.6)
print(f'A probabilidade de a Sara ganhar é {p3:.3f}')
