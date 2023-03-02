#!/usr/bin/env python

# RNA Splicing

from Bio.Seq import Seq
from Bio import SeqIO

data = SeqIO.parse("data/rosalind_splc.txt","fasta")
target = str(next(data).seq)

for intron in data:
    target = target.replace(str(intron.seq),"")
rna_splc = Seq(target).translate()[:-1]

print (rna_splc)