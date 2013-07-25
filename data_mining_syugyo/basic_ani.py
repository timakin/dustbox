import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np
np.random.seed(0)

mu,sig = 100, 15
data = mu + sig*np.random.randn(10000)

fig = plt.figure(1)

gs = GridSpec(2,1, height_ratios=[4,1], hspace=0.05)
ax1 = fig.add_subplot(gs[0,0])
ax1.set_xticklabels([])
ax1.set_xlim(0,data.max())
ax1.set_ylabel('freq')
ax1.grid(True)
n, bins, patches = ax1.hist(data,100)

ax2 = fig.add_subplot(gs[1,0])
ax2.set_xlim(0,data.max())
ax2.set_ylim(0,1.0)
ax2.set_ylabel('accum. ratio')
ax2.set_xlabel('value')
ax2.grid(True)
n, bins, patches = ax2.hist(data,100, cumulative=True,normed=True,histtype='step')

label_text=r'''
 $n = %d$
 $\mu = %.2f$
 $\sigma = %.2f$''' % (len(data), data.mean(), data.std(), )
label = ax2.text( 0 , 0.98 , label_text)
label.set_verticalalignment('top')
label.set_horizontalalignment('left')

fig.show()
raw_input()
