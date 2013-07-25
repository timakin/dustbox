#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl
import matplotlib.mlab as mlab

mu=0
sigma=1
rnum = np.random.normal(mu, sigma, 10000) #random number ,平均と標準偏差
n, bins, patches = pl.hist(rnum, bins=40, range=(-4, 4), normed=True)
pl.hist(rnum, bins = 1000, range=(-4, 4), normed=True, cumulative=True, histtype='step')
#bins=棒の数,range=値の範囲,normed=標準化
line = mlab.normpdf( bins, 0, 1)
pl.ylabel("probability",fontsize=18)
pl.xlabel("value",fontsize=18)
pl.legend(loc="upper left")
pl.plot(bins, line, 'r-', linewidth=2)
pl.show()