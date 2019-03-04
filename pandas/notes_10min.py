# https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series([1, 2, 3, np.nan, 6, 8])

t = pd.Series([11, 22, np.nan, 33, 66, 88])
pd.concat([s, t])
df_1: pd.DataFrame = pd.concat([s, t], axis=1)
df_1.rename({0: "hi", 1: "ho"})  # rows
df_1.rename(index={0: "hi", 1: "ho"})  # rows
df_1.rename(columns={0: "hi", 1: "ho"})  # columns

dates = pd.date_range('20130101', periods=6)
pd.date_range('20130101', periods=6, freq='H')  # hours
len(pd.date_range('20130101', '20130102', freq='H', closed='left'))  # 24

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
df

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})

df2
df2.dtypes
df2.A

df.head()
df.tail(3)
df.sample(2)
df.index
df.columns
df.describe()  # summary of data
df.to_numpy()  # expensive if not already uniform in type
df.T  # transpose
df.sort_index(axis=1, ascending=False)
df.sort_values(by="A", ascending=False)  # sort rows by a column
df.sort_values(axis=1, by="2013-01-02")  # sort columns by a row

df.loc['20130102':'20130104', ['A', 'B']]
df.loc['20130102', ['A', 'B']]

df[df.A > 0]
df[df > 0]

df2 = df.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
df2
df2[df2['E'].isin(['two', 'three'])]
df2[df2.loc[:, 'D'] < 0]

df2.iloc[3, 5] = np.nan  # Note: column E has dtype = object
del df2['E']  # delete column E

s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102', periods=6))
s1
df
df['F'] = s1  # drops last value of series since the index does not appear in the df
df

pd.concat([df, s1], axis=1)  # enlarges both

df.at[dates[0], 'A'] = 0

df2 = df.copy()
df2[df2 < 0] = -df2
df3 = df.copy()
df3[df3 > 0] = np.nan

df.dropna()
df.fillna(value=999)
df.isna()

df.mean()
df.mean(axis=1)

s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
df.sub(s, axis='index')

df.apply(np.cumsum)
df.apply(np.cumsum, axis=1)
df.apply(lambda x: x.max() - x.min(), axis=1)

s = pd.Series(np.random.randint(0, 7, size=10))
s.value_counts()

# Using these methods / indexers, you can chain data selection operations without using temporary variable.
df.loc[lambda df: df.A > 0, :]
df.loc[:, lambda df: ['A', 'B']]

df.append(df.iloc[2])
df.append(df.iloc[2], ignore_index=True)

df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                         'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three',
                         'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})

df.groupby('A').sum()
df.groupby(['A', 'B']).sum()

tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                     'foo', 'foo', 'qux', 'qux'],
                    ['one', 'two', 'one', 'two',
                     'one', 'two', 'one', 'two']]))
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
df.stack()
df.stack().unstack(0)

df = pd.DataFrame({"A": ["foo", "foo", "foo", "foo", "foo",
                         "bar", "bar", "bar", "bar"],
                   "B": ["one", "one", "one", "two", "two",
                         "one", "one", "two", "two"],
                   "C": ["small", "large", "large", "small",
                         "small", "large", "small", "small",
                         "large"],
                   "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
                   "E": [2, 4, 5, 5, 6, 6, 8, 9, 9]})
pd.pivot_table(df, index=['A'], columns=['B'], values='D', aggfunc=np.sum)
pd.pivot_table(df, index=['A'], columns=['B'], values='D', aggfunc=np.mean)

df = pd.DataFrame({"id": [1, 2, 3, 4, 5, 6], "raw_grade": ['a', 'b', 'b', 'a', 'a', 'e']})
df["grade"] = df["raw_grade"].astype("category")
df["grade"].cat.categories = ["very good", "good", "very bad"]
df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])
df['grade'].value_counts()
df.sort_values(by='grade')

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()
plt.show()
