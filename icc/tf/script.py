# Trabalho grupo Ramon Moreira

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('~/unb/icc/tf/complete.csv')

plt.hist(df.overall, bins = 16)
plt.xlabel('Nível \"overall"')
plt.ylabel('Frequência')

plt.scatter(df.overall, df.eur_value, c = df.eur_value)
plt.xlabel('Nível \"overall"')
plt.ylabel('Preço (10e8 €)')

df2 = df.head(1000).groupby(['league'])['overall'].mean()
df2.sort_values().plot.barh()
