import matplotlib.pyplot as plt
import pandas as pd

import prince


df = pd.read_csv('data/woman_work.csv', index_col=0)
df = df[['Stay at home','Part-time work','Full-time work']]

ca = prince.CA(df, n_components=-1)

#fig1, ax1 = ca.plot_cumulative_inertia()
fig2, ax2 = ca.plot_rows_columns(show_row_labels=True, show_variable_labels=True)

plt.show()
