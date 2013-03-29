#!/usr/bin/env python
# -*- coding: utf-8 -*-

def weightedmean(w, x):
	n = len(w)
	num = sum([w[i]*x[i] for i in range(n)])
	den = sum([w[i] for i in range(n)])
	if den==0: return 0
	r = num/den
	return r