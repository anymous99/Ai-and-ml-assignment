import pandas as pd
import numpy as np

df = pd.DataFrame([[1, 2, np.nan, 4], [2, 3, 4, 5],
                  [3, 4, 5, 6], [0, 0, 1, 1]])
df.columns = ['Random 1', 'Random 2', 'Random 3', 'Random 4']

print(df.describe())

print(df.isnull().any())

print(df.info())

print(df.loc[2])

print(df.loc[3])
