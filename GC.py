#!/usr/bin/env python

# Computing GC Content
from Bio import SeqIO
from Bio.SeqUtils import GC

gc_per = 0
gc_id = ""

file = open('data/rosalind_gc.txt', 'r')
for record in SeqIO.parse(file, 'fasta'):
    if gc_per < GC(record.seq):
        gc_per = GC(record.seq)
        gc_id = record.id

print (gc_id)
print (gc_per)
