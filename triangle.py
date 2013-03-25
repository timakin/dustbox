#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import math

class Triangle:
	def __init__(self, n, a):
		self.n = n
		self.a = a

	def solve(self, n, a):
		self.n = n
		self.a = a
		ans = 0
		for i in xrange(0,n):
			for j in xrange(i+1,n):
				for k in xrange(j+1,n):
					leng = self.a[i] + self.a[j] + self.a[k]
					ma = max(self.a[i], max(self.a[j], self.a[k])) 
					rest = leng-ma

					if ma>rest:
						ans = max(ans, leng)
		
if __name__ == '__main__':
	test = Triangle(5,[2,3,4,5,10])
	print test.a
	print test.n
	print test.solve(5,[2,3,4,5,10])
