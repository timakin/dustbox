#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl
 
abc = np.random.normal(0, 1, 10000)    #平均値=0, sigma=1の分布を持つランダムデータ作成
pl.hist(abc, bins=40, range=(-5, 5), normed=True)
pl.show()