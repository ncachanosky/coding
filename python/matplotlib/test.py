# %% | IMPORT PACKAGES
import  numpy               as np
import  matplotlib.pyplot   as plt
from    matplotlib          import style


# %% | MATPLOTLIB STYLE AND FORMATS
# plt.style.use('my-paper')
plt.style.use('https://github.com/ncachanosky/coding/blob/main/python/matplotlib/my-UTEP.mplstyle?raw=true')


# %% | PLOT EXAMPLE

plt.style.use('C:/Users/ncachanosky/OneDrive/GitHub/coding/python/matplotlib/my-UTEP.mplstyle')

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3]);  # Plot some data on the axes.
plt.title("My title", size="xx-large")
