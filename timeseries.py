#!/usr/bin/env python

import sys
from math import *
import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

times = pd.read_csv('067_Hiashi.csv', names=['date','begin', 'high', 'low', 'end'], skiprows=1, header=None)
x = times['date'].apply(pd.to_datetime)
means = (times['high']+times['low'])/2

ts_1st = pd.DataFrame(times.end.values, index=x, columns=['end'])
ts_2nd = pd.DataFrame(times.begin.values, index=x, columns=['begin'])
ts_3rd = pd.DataFrame(times.high.values, index=x, columns=['high'])
ts_4th = pd.DataFrame(times.low.values, index=x, columns=['low'])
ts_5th = pd.DataFrame(means.values, index=x, columns=['mean'])

a=pd.merge(ts_1st, ts_2nd, left_index=True, right_index=True)
b=pd.merge(a, ts_3rd, left_index=True, right_index=True)
c=pd.merge(b, ts_4th, left_index=True, right_index=True)
d=pd.merge(c, ts_5th, left_index=True, right_index=True)

print d.head()

plt.plot(x, ts_5th)
plt.bar(x, (times['high']-times['low'])*2)
plt.xlabel('Date', size=20)
plt.ylabel('Activity of Stock', size=20)
plt.show()
