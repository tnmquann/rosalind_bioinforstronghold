#!/usr/bin/env python

# Counting Nucleotides
seq = input("Enter a DNA sequence: ")
# Define a list of DNA nucleotides
DNA_Nucleotides = ["A", "C", "G", "T"]

# Define a function that validates a DNA sequence
def validate_seq(seq):
  seq = seq.upper()
  for nuc in seq:
    if nuc not in DNA_Nucleotides:
      return False
  return seq

# Define a function that counts the frequency of each nucleotide in DNA sequence
def count_nuc_freq(seq):
  freq_dict = {"A":0, "C":0, "G":0, "T":0}
  for nuc in seq:
    freq_dict[nuc] += 1
  return freq_dict

seq = validate_seq(seq)
freq_dict = count_nuc_freq(seq)
print(freq_dict)