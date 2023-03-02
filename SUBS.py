#!/usr/bin/env python

# Finding a Motif in DNA
a, b = open('data/rosalind_subs.txt').read().split()

locations = []
for i in range(0, len(a)-len(b)+1):
    if a[i:i+len(b)] == b:
        locations.append(str(i+1))

with open('output/SUBS.txt', 'w') as output_dat:
    output_dat.write(' '.join(locations))
