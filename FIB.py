#!/usr/bin/env python

# Rabbits and Recurrence Relations

def fib(n,k):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1,k) + k*fib(n-2, k)

with open('data/rosalind_fib.txt') as input_data:
	rab_month,rab_pairs = map(int, input_data.read().split())

rabbits = str(fib(rab_month,rab_pairs))
print(rabbits)

"""
Cách 2. Giải theo hướng lập công thức
(1) Dãy số cần tìm có dạng: $x_n=x_{n-1}+k\cdotx_{n-2}$
(2) Dưa dãy về dạng phương trình tổng quát: $x^2=x+k$
(3) Đặt nghiệm của phương trình trên là $x_{1}, \quad x_{2}$. Công thức số hạng tổng quát của dãy: $x_n=\alpha x_1^{n} + \beta x_2^{n}$
(4) Thế một vài giá trị ban đầu để tính giá trị $\alpha$ và $\beta$.

Vậy công thức cho bài toán này có thể viết dưới dạng:
$$f(n) = \frac{\sqrt{4k+1} \left(1-\sqrt{4k+1}\right)^n-\left(1-\sqrt{4k+1}\right)^n+\sqrt{4k+1}\left(\sqrt{4k+1}+1\right)^n+\left(\sqrt{4k+1}+1\right)^n}{2^{n+1}\sqrt{4k+1}}$$
"""
