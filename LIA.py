#!/usr/bin/env python
"""
Hint: Use Binomial Expansion
"""
# Independent Alleles
from scipy.special import comb

with open('data/rosalind_lia.txt') as input_data:
	k, N = map(int, input_data.read().split())

pr = 0
for i in range(N, 2**k + 1):
    pr += comb(2**k, i) * ((1/4.0)**i) * ((3/4.0)**((2**k)-i))

print(pr)