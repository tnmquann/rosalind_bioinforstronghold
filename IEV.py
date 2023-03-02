#!/usr/bin/env python

# Calculating Expected Offspring
"""
Xác suất đời con mang gene trội
AA x AA -> 1
AA x Aa -> 1
AA x aa -> 1
Aa x Aa -> 0.75
Aa x aa -> 0.5
aa x aa -> 0
"""
with open('data/rosalind_iev.txt') as file:
	str = file.read().split()
p_list = [1, 1, 1, 0.75, 0.5, 0]
EV_list =[]

for index, num_parents in enumerate(str):
    EV_list.append(2*int(num_parents)*p_list[index])

print (sum(EV_list))