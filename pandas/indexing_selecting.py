# https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html

# axis labeling: identifies data, enables automatic and explicit data alignment, allows getting and setting of subsets
#  of the data

# Warning: sometimes a copy or reference of the data is returned.  When setting data avoid chained assignment.

# use .loc and .iloc
# use [] for selecting lower dimensional slices

import pandas as pd
import numpy as np

df1 = pd.DataFrame({'a': np.arange(4), 'b': np.arange(1, 5), 'd': np.arange(2, 6)})


df1[['a', 'b']] = df1[['b', 'a']]          # this reverses columns, repeat to reverse back
df1.loc[:, ['a', 'b']] = df1[['b', 'a']]   # this does not reverse columns, b/c columns are aligned before assignment
df1.loc[:, ['a', 'b']] = df1[['b', 'a']].to_numpy()   # this does swap b/c in getting the raw values the alignment info
                                                      # is dropped

# .loc: purely label based indexing
# in slices start and end are included

# .iloc: purely integer based indexing
# in slices start is included, end is not -> as in python and numpy is usual

# both .loc and .iloc can take a callable as argument, can be used to avoid assigning a temporary variable

df1.loc[lambda df: df.a >= 1]  # in this example imagine first doing some operations on df1 chaning the contends
                               # chaning which rows are selected (possibly)

# don't index with missing labels, use reindex in stead.

# selecting random .sample arguments n for count, and weights if want weighted sample

# .at label based scalar lookups, .iat integer based scalar lookups.  They are more efficient b/c can avoid some overhead.
