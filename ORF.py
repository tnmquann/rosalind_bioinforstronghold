#!/usr/bin/env python

# Open Reading Frames
from Bio import SeqIO
from Bio.Seq import Seq
import re
import itertools
import bisect

record = SeqIO.read("data/rosalind_orf.txt","fasta")
dna_f = str(record.seq)
dna_r_comp = str(Seq(dna_f).reverse_complement())

proteins = []
def orf(dna):
    frames = []
    for i in range(3):
        dna_tr_i = str(Seq(dna[i:]).translate())
        frames.append(dna_tr_i)

    for frame in frames:
        frame = frame.replace('*', 'B')
        start_position = [m.start() for m in re.finditer('M', frame)]
        stop_position = [m.start() for m in re.finditer('B', frame)]  
        for start in start_position:                  
            if start < max(stop_position):
                protein_stop = stop_position[bisect.bisect(sorted(stop_position), start)]
                proteins.append(frame[start:protein_stop])                  

orf(dna_f)
orf(dna_r_comp) 

for p in list(set(proteins)):
    print(p)