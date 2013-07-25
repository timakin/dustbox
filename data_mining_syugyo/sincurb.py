from scipy import *
import pylab as pl


x = arange(0,2*pi,0.01)
y = sin(x)
pl.plot(x,y)
pl.show()