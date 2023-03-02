#!/usr/bin/env python
from scipy.special import comb

with open('data/rosalind_iprb.txt') as input_data:
    hom, het, rec = map(int, input_data.read().split())

sample_space = comb(hom+het+rec, 2)
rec_chosen = 1*comb(rec, 2) + 0.5*rec*het + 0.25*comb(het, 2)

print(1 - rec_chosen/sample_space)

"""
Ta quy về bài toán tìm xác suất xuất hiện cá thể đồng hợp lặn (aa)
Gọi A > a. Các phép lai cho được cá thể đồng hợp lặn là phép lai giữa các cá thể dị hợp & đồng hợp lặn.
Aa x Aa -> 1/4aa ; aa x aa -> 1aa ; Aa x aa -> 1/2aa
Không gian mẫu: $C^{2}_{k+m+n}
Cách chọn cho Aa x Aa: $\dfrac{1}{4}\times C^{2}_{m}$
Cách chọn cho Aa x Aa: $\dfrac{1}{2}\times m \times n$
Cách chọn cho aa x aa: $C^{2}_{n}$
"""