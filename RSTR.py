#!/usr/bin/env python

# Matching Random Motifs
"""
Tình số lượng CG và AT. Từ bài PROB.py, xác suất cho G+C là $\dfrac{x}{2}, A+T là $\dfrac{1-x}{2}$
Xác suất nhận được trình sự giống ${s}$ là $p = \left(\dfrac{x}{2}^{C+G}\times$\dfrac{1-x}{2}$^{A+T}\right)$.
Xác suất thu được trình tự ít nhất 1 lần trong ${N}$ lần thử = 1 - Pr(xác suất không bao giờ nhận được trình tự) = 1 - (1 - p)^N
"""
# Matching Random Motifs

with open("data/rosalind_rstr.txt", "r") as f:
    N, x = f.readline().strip().split(" ")
    N = int(N)
    x = float(x)
    str = f.readline().strip()

sum_AT = str.count('A') + str.count('T')
sum_GC = str.count('G') + str.count('C')
pr = pow(x/2, sum_GC) * pow((1-x)/2, sum_AT)
print(1 - pow(1 - pr, N))