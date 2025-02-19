"""
======
pie(X)
======

See `~matplotlib.axes.Axes.pie`.
"""
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('mpl_plot_gallery')


# make data
X = [1, 2, 3, 4]
colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(X)))

# plot
fig, ax = plt.subplots()
ax.pie(X, colors=colors, radius=3, center=(4, 4),
       wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()
