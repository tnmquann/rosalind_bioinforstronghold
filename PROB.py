#!/usr/bin/env python

from math import log10

with open('data/rosalind_prob.txt') as input_data:
	dna, gc_content = input_data.readlines()
gc_content = map(float, gc_content.split())

# Counts in the number of G+C codons in index 0 and A+T codons in index 1.
codon_count = [0, 0]
for codon in dna:
	if codon in ['C', 'G']:
		codon_count[0] += 1
	elif codon in ['A', 'T']:
		codon_count[1] += 1


"""
Shortcut:
$\log_{10}{\left(\frac{x}{2}\right)^{g + c} \left(\frac{1-x}{2}\right)^{a + t}} = \left(g + c\right)\log_{10}{\frac{x}{2}} + \left(a + t\right)\log_{10}{\frac{\left(1- x\right)}{2}}$
"""
gc_prob = []
for gc_value in gc_content:
	log_prob = codon_count[0]*log10(0.5*gc_value) + codon_count[1]*log10(0.5*(1-gc_value))
	gc_prob.append(str(log_prob))

with open('output/PROB.txt', 'w') as output_file:
	output_file.write(' '.join(gc_prob))