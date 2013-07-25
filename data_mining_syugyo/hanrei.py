#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pylab

x = pylab.arange(-2, 2, 0.1)
sin_ = pylab.sin(x)
cos_ = pylab.cos(x)

pylab.subplot(211)
pylab.plot(x, sin_, 'r-')
pylab.plot(x, cos_, 'b-.') 
pylab.legend(('testsin', 'cos'), 'upper left')

pylab.subplot(212)
pylab.plot(x, sin_, 'm-', label="simulation")
pylab.plot(x, cos_, 'g-.', label="test") #プロットデータ指定
pylab.legend(loc = 'upper left')
pylab.suptitle('legend test', fontsize=30)
pylab.show()