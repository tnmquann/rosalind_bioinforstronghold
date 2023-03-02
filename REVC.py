#!/usr/bin/env python

# Complementing a Strand of DNA
def complement_dna(seq):
  seq = seq.upper()
  complement_dict = {"A":"T", "T":"A", "G":"C", "C":"G"}
  # Initialize an empty string to store the complemented sequence
  complement_seq = ""

  for nuc in seq:
    # If the nucleotide is not valid, append 'N' instead
    if nuc not in complement_dict:
      complement_seq += 'N'
    else:
      complement_seq += complement_dict[nuc]
  return complement_seq

# Get the input from the user
DNA_REVC = input("Enter a DNA sequence: ")
complement_seq = complement_dna(DNA_REVC)
seq_reverse = complement_seq[::-1]
print(seq_reverse)