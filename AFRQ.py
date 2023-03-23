#!/usr/bin/env python


from math import sqrt

with open('data/rosalind_afrq.txt') as input_data:
	A = map(float, input_data.read().strip().split())

B = [2*sqrt(i)-i for i in A]

print ' '.join(map(str,B))
with open('output/065_AFRQ.txt', 'w') as output_data:
	output_data.write(' '.join(map(str,B)))