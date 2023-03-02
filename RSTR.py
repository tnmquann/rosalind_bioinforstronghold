#!/usr/bin/env python

"""
First count the C/Gs and A/Ts. The probability that any given letter is A is (1-x)/2, as is T, and the probability that a letter is C is x/2, as is G.
The probability of getting a sequence S is p = ( P(C) ^ (#ofC+G) * P(A) ^ (#ofA+T) ).
The probability of getting the sequence at least once in N tries is the same a 1 minus the probability of never getting it, which is equal to (1 - p) ^ N. Thus the answer is 1 - (1 - p) ^ N
"""
# Matching Random Motifs

with open("data/rosalind_rstr.txt", "r") as f:
    N, x = f.readline().strip().split(" ")
    N = int(N)
    x = float(x)
    s = f.readline().strip()

at = s.count('A') + s.count('T')
gc = s.count('G') + s.count('C')
P_s = pow(x/2, gc) * pow((1-x)/2, at)
print(1 - pow(1 - P_s, N))