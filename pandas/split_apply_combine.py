"""Group By: split-apply-combine

Notes: https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame([('bird', 'Falconiformes', 389.0),
                   ('bird', 'Psittaciformes', 24.0),
                   ('mammal', 'Carnivora', 80.2),
                   ('mammal', 'Primates', np.nan),
                   ('mammal', 'Carnivora', 58)],
                  index=['falcon', 'parrot', 'lion', 'monkey', 'leopard'],
                  columns=('class', 'order', 'max_speed'))

grouped = df.groupby('class')
grouped2 = df.groupby('order', axis='columns')  # <= no comprehension of this at all yet
grouped3 = df.groupby(['class', 'order'])

df.groupby('class').apply(lambda x: print(f"group {x}"))  # Note first group is printed twice

grouped3.mean()
df.fillna(9900).groupby(['class', 'order']).mean()

grouped.max()
grouped['max_speed'].max()
# Series has the name max_speed.  grouped['max_speed'] is just that column under the grouping

df2 = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                          'foo', 'bar', 'foo', 'foo'],
                    'B': ['one', 'one', 'two', 'three',
                          'two', 'two', 'one', 'three'],
                    'C': np.random.randn(8),
                    'D': np.random.randn(8),
                    'E': np.arange(8) + 11})

df3 = df2.set_index(['A', 'B'])
grouped4 = df3.groupby(level=df3.index.names.difference(['B']))


def get_letter_type(letter):
    if letter.lower() in 'aeiou':
        return 'vowel'
    else:
        return 'consonant'


grouped5 = df2.groupby(get_letter_type, axis=1)

arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
          ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
index = pd.MultiIndex.from_arrays(arrays, names=['first', 'second'])
s = pd.Series(np.arange(8), index=index)
s.groupby(level=1).sum()
s.groupby(level=0).sum()


index = pd.date_range('10/1/1999', periods=1100)
ts = pd.Series(np.random.normal(0.5, 2, 1100), index)
