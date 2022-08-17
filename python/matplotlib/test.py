# %% | IMPORT PACKAGES
import  numpy               as np
import  matplotlib.pyplot   as plt
from    matplotlib          import style


# %% | MATPLOTLIB STYLE AND FORMATS
# plt.style.use('my-paper')
plt.style.use('https://github.com/ncachanosky/coding/blob/main/python/matplotlib/Style_UTEP?raw=true')

# %% | PLOT EXAMPLE
fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3]);  # Plot some data on the axes.

# %%
