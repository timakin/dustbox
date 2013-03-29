#!/usr/bin/env python
# -*- coding: utf-8 -*-

#2変数にどの程度創刊が見れられるかを示す数値

def peason(x, y):
	n = len(x)
	vals = range(n)

	sumx = sum([float(x[i]) for i in vals])
	sumy = sum([float[y[i]] for i in vals])
	
	sumx2 = sum([x[i]**2.0 for i in vals])
	sumy2 = sum([y[i]**2.0 for i in vals])

	sumxy = sum([x[i]*y[i] for i in vals])

	num = sumxy -(sumx*sumy/n)
	den = ((sumx2-pow(sumx, 2)/n)*(sumy2-pow(sumy, 2)))
	if den==0 : return 0
	r = num/den
	return r