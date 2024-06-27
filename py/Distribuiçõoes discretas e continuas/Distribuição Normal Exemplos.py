from scipy import stats

# A probabilidade de um relogio durar mais de 11 anos é
# P(T > 11) = 1 − P(T ≤ 11).
p1 = 1 - stats.norm.cdf(11, 11, 1)
print(f'A prob. de um relógio durar mais de 11 anos é {p1:.3f}')

# A probabilidade de um relogio durar menos de 10 anos é
# P(T < 10).
p2 = stats.norm.cdf(10, 11, 1)
print(f'A prob. de um relógio durar menos de 10 anos é {p2:.3f}')

# Pretendemos descobrir o tempo t (em anos), tal que
# P(T < t) = 0.05.
t = stats.norm.ppf(0.05, 11, 1)
print(f'O periodo de garantia, se a fabrica nao prtender substituir mais do que 5% dos relogios é {t:.3f} anos')

# Qual a probabilidade de pelo menos dois deles durarem mais de 12 anos? Sejam,
# X = numero de relogios que duram mais de 12 anos
# n = 5, numero de relogios comprados
# p = P(T > 12) = 1 − P(T ≤ 12) = 0.159
# X ∼ Bi(n = 5, p = 0.159).
# A probabilidade pedida ´e dada por P(X ≥ 2) = 1 − P(X ≤ 1).
p = 1 - stats.norm.cdf(12, 11, 1)
p3 = 1 - stats.binom.cdf(1, 5, p)
print(f'A prob. de pelo menos 2 deles durarem mais de 12 anos é {p3:.3f}')

# Qual a probabilidade de pelo menos um deles durar menos de 10 anos? Sejam,
# X = numero de relogios que duram menos de 10 anos
# n = 5, numero de relogios comprados
# p = P(T < 10) = 0.159
# X ∼ Bi(n = 5, p = 0.159).
# A probabilidade pedida ´e dada por P(X ≥ 1) = 1 − P(X = 0).
p_2 = stats.norm.cdf(10, 11, 1)
p4 = 1 - stats.binom.pmf(0, 5, p_2)
print(f'A prob. de pelo menos 1 deles durar menos de 10 anos é {p4:.3f}')