#!/usr/bin/env python

# Transitions and Transversions

from Bio import SeqIO

transition = [('A', 'G'), ('T', 'C'), ('C', 'T'), ('G', 'A')]
transversions = [('A', 'T'), ('A', 'C'), ('T', 'A'), ('T', 'G'), ('C', 'A'), ('C', 'G'), ('G', 'T'), ('G', 'C')]

seq_name, seq_str = [], []
with open ("data/rosalind_tran.txt",'r') as f:
    for seq_rec  in SeqIO.parse(f,'fasta'):
        seq_name.append(str(seq_rec.name))
        seq_str.append(str(seq_rec.seq))

transition_c, transversions_c = 0, 0
seq_1, seq_2 = seq_str

for i in range(len(seq_1)):
    if (seq_1[i], seq_2[i]) in transition:
        transition_c += 1
    if (seq_1[i], seq_2[i]) in transversions:
        transversions_c += 1
print(transition_c/transversions_c)