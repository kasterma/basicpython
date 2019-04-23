import pandas as pd
import numpy as np
import random

df1 = pd.DataFrame({'A': range(20), 'B': range(20), 'C': random.choices([1, 2, 3], k=20)})
df2 = pd.DataFrame({'A': range(10), 'B': range(10), 'C': random.choices([1, 2, 3], k=10)})
pd.crosstab(df2.A, df1.A)

pd.concat([df1, df2], axis=1)
pd.concat([df1, df2], axis=1).dtypes

df1['A'].map(pd.Series([11,22,33]))
df1['A'].map(pd.Series([11,22,33])).map(lambda x: x + 3)
df1['A'].map(pd.Series([11,22,33])).map(lambda x: f"yo {x} yo")
df1['A'].map(pd.Series([11,22,33])).map(lambda x: f"yo {x} yo", na_action='ignore')
