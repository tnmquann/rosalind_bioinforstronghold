#!/usr/bin/env python

def hamm(seq_1, seq_2):
    dist = 0
    assert len(seq_1) == len(seq_2)
    for i in range(len(seq_1)):
        if seq_1[i] != seq_2[i]:
            dist += 1
    return dist

with open("data/rosalind_hamm.txt", "r") as f:
    seq_1 = f.readline().strip()
    seq_2 = f.readline().strip()
print(hamm(seq_1, seq_2))