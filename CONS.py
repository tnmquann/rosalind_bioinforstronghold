#!/usr/bin/env python

# Consensus and Profile
import sys
from Bio import SeqIO
import numpy as np
np.set_printoptions(threshold=np.inf)

seq_name, seq_str = [], []
with open ('data/rosalind_cons.txt','r') as fa:
    for seq_rec in SeqIO.parse(fa,'fasta'):
        seq_name.append(str(seq_rec.name))
        seq_str.append(str(seq_rec.seq))

seq_len = len(seq_str)
str_len = len(seq_str[0])

symbol = ['A', 'C', 'G', 'T']
consensus_string = ''
matrix_row = np.zeros(shape=(4, str_len), dtype=int)

for k in range(str_len):
    position_symbol = [s[k] for s in seq_str]
    most_common_symbol = max(position_symbol, key=position_symbol.count)
    consensus_string += most_common_symbol
    for j in range(len(symbol)):
        matrix_row[j][k] = position_symbol.count(symbol[j])
    
print(consensus_string)
for i in range(len(symbol)):
    print("{}: {}".format(symbol[i], " ".join([str(j) for j in matrix_row[i]])))