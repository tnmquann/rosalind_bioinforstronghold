#!/usr/bin/env python

# Mortal Fibonacci Rabbits

with open('data/rosalind_fibd.txt') as input_data:
    n,k = map(int, input_data.read().split())

def fib(n,k=1):
  ages = [1] + [0]*(k-1)
  for i in range(n-1):
    ages = [sum(ages[1:])] + ages[:-1]
  return sum(ages)

Total_Rabbits = fib(n,k)

print(Total_Rabbits)