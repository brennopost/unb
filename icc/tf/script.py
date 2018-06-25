import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('~/unb/icc/tf/complete.csv')
plt.hist(df.overall, bins = 18)

plt.scatter(df.overall, df.eur_value, c = df.eur_value)

plt.bar(df.league, df.overall)
