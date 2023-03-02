#!/usr/bin/env python

def hamm(str1, str2):
    distance = 0
    assert len(str1) == len(str2)
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1
    return distance

with open("data/rosalind_hamm.txt", "r") as f:
    str1 = f.readline().strip()
    str2 = f.readline().strip()
print(hamm(str1, str2))