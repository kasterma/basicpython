import pandas as pd

x1 = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['a', 'b'], index=pd.RangeIndex(2, 5))
x2 = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['a', 'b'], index=pd.RangeIndex(1, 4))

pd.concat([x1, x2], axis=1)
x3 = pd.concat([x1, x2])
x3.loc[2, ['b']]
x3.iloc[[2]]
x3.loc[[1]]

x3.loc[1]  # this is a Series
x3.loc[2]  # this is a DataFrame
x3.loc[[1]]
x3.loc[[2]]  # are both dataframes.

d1 = pd.DataFrame({'a': [1, 2, 3]})
d1['b'] = d1['a'] * 11
d2 = pd.DataFrame({'a': [2, 3, 4]})
d2['c'] = d2['a'] * 11
