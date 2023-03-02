#!/usr/bin/env python

# Locating Restriction Sites

from Bio import SeqIO

def switch(str):
    str = str[::-1]
    switch_str = ''
    for i in range(len(str)):
        if str[i] == 'A':
            switch_str += 'T'
        elif str[i] == 'T':
            switch_str += 'A'
        elif str[i] == 'G':
            switch_str += 'C'
        elif str[i] == 'C':
            switch_str += 'G'
    return switch_str

def palindrome(str):
    for i in range(len(str)):
        for j in range(4,13,1):
            if str[i:i+j] == switch(str[i:i+j]) and (i+j <= len(str)):
                print(i+1, j)


seq_name, seq_string = [], []

with open ('data/rosalind_revp.txt','r') as f:
    for seq_record  in SeqIO.parse(f,'fasta'):
        seq_name.append(str(seq_record.name))
        seq_string.append(str(seq_record.seq))

seq = seq_string[0]
palindrome(seq)