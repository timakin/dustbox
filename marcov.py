#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import math
import random

def main():
	f = lambda x: math.exp(-x*x / 10.0)
	for x, fx in metropolis(f):
		print x, fx


def metropolis(func, start=0.0, delta=2.0, burn_in=100, seed=1):
	metro_iter = _metropolis(func, start, delta, seed)
	for i, value in enumerate(metro_iter):
		if i > burn_in:
			yield value
			break
	for value in metro_iter:
		yield value

def _metropolis(func, start, delta, seed):
	random.seed(seed)
	initial_x = start
	initial_fx = func(initial_x)
	proposed_x, proposed_fx = 0.0, 0.0
	while True:
		proposed_x = initial_x + random.uniform(-delta, delta)
		proposed_fx = func(proposed_x)
		ratio  =proposed_fx / initial_fx
		if ratio > 1.0 or ratio > random.random():
			initial_x, initial_fx = proposed_x, proposed_fx
			yield proposed_x, proposed_fx
		else:
			yield initial_x, initial_fx


if __name__ == '__main__':
	sys.exit(main())