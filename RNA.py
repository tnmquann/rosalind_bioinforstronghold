#!/usr/bin/env python

# DNA transcription
# Define a function that converts a DNA sequence to an RNA sequence
def dna_to_rna(seq):
  seq = seq.upper()
  seq = seq.replace('T', 'U')
  return seq

# Input
dna_seq = input("Enter a DNA sequence: ")
rna = dna_to_rna(dna_seq)
print(rna)