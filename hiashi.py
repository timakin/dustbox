import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

days, impressions = np.loadtxt("page-impressions.csv", skiprows=1, unpack=True, converters={0: mdates.strpdate2num('%Y-%m-%d'): })
plt.plot_date(x=days, y=impressions, fmt="-r")
plt.show()