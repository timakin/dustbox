#!/usr/bin/env python
# -*- coding: utf-8 -*-

#ユークリッド距離は、2つの値の関係性を調べるときに
#用いられる数式である。多次元空間中での個別の点の距離を測るための数式。


import math

def euclidian(p,q):
	sum = 0
	for i in range(len(p)):
		sum += (p[i]-q[i])**2

	return math.sqrt(sum)

if __name__ == '__main__':
	p = [1,2,3,4]
	q = [2,4,6,8]
	print euclidian(p,q)