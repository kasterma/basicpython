# Notes on http://tomaugspurger.github.io/modern-1.html

# imports as from page

import zipfile

import requests
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import unittest

class Modern1(unittest.TestCase):
    def test_ix_indexing(self):
        # .ix is a general indexer, but b/c it has two different ways of operation (if there is are an integer
        # index lookup by index values, if there is another type of index lookup by row number) knowledge of the
        # object is needed to know how the result is obtained.  Safer to use .loc/.iloc
        test_dat = {'i': np.arange(10), 'a': np.random.rand(10), 'b': np.random.rand(10)+4}
        test_df = pd.DataFrame(test_dat)

        test_df['a']
        test_df.ix[[1, 2, 3], ['b', 'a']]

        test_dat = {'i': np.arange(10), 'a': np.random.rand(10), 'b': np.random.rand(10)+4}
        test_df = pd.DataFrame(test_dat, index=np.arange(10,20))

        test_df.ix[[1, 2, 3]]

    def test_lociloc_indexing(self):
        test_dat = {'i': np.arange(10), 'a': np.random.rand(10), 'b': np.random.rand(10) + 4}
        test_df = pd.DataFrame(test_dat, index=np.arange(10, 20))
        test_df.iloc[[1, 2, 3]]
        with self.assertRaisesRegex(KeyError, "None of \[\[1, 2, 3\]\] are in the \[index\]"):
            test_df.loc[[1, 2, 3]]
        with self.assertRaisesRegex(IndexError, "positional indexers are out-of-bounds"):
            test_df.iloc[[1, 2, 11]]
        test_df.loc[11, ['b', 'i']]

    def test_drop_dim(self):
        # depending on the shape of the indices used, the output will be of a different shape
        test_dat = {'i': np.arange(10), 'a': np.random.rand(10), 'b': np.random.rand(10) + 4}
        test_df = pd.DataFrame(test_dat, index=np.arange(10, 20))
        self.assertEquals(test_df.loc[11:11,['b']].shape, (1,1))
        self.assertEquals(test_df.loc[11:11,'b'].shape, (1,))
        self.assertEquals(test_df.loc[11,'b'].shape, ())

    def test_generate_SetttingWithCopy_error(self):
        test_dat = {'i': np.arange(10), 'a': np.random.rand(10), 'b': np.random.rand(10) + 4}
        test_df = pd.DataFrame(test_dat, index=np.arange(10, 20))

        a = test_df['a']
        a[10] = 4                  # warning, but value is set

        test_df['a'][10] = 5       # warning, but value is set

        # from
        # http://pandas-docs.github.io/pandas-docs-travis/indexing.html?highlight=view#indexing-view-versus-copy
        dfmi = pd.DataFrame([list('abcd'), list('efgh'), list('ijkl'), list('mnop')],
                            columns = pd.MultiIndex.from_product([['one', 'two'], ['first', 'second']]))
        dfmi['one']['second'] = 3  # warning, value not set
        self.assertEquals(dfmi.loc[0, ('one', 'second')], 'b')

        a = dfmi['one']
        a['second'] = 4
        self.assertEquals(a.loc[0, 'second'], 4)
        self.assertEquals(dfmi.loc[0, ('one', 'second')], 'b')

    def test_generate_multiindices(self):
        test_dat = {'i': np.arange(10), 'a': np.random.rand(10), 'b': np.random.rand(10) + 4}
        test_df = pd.DataFrame(test_dat, index=pd.Index(np.arange(10, 20), name = "idx1"))
        test_df1 = test_df.set_index(['a'], append=True)
        self.assertEquals(test_df1.index.names, ['idx1', 'a'])
        test_df2 = test_df.set_index(['a', 'b'])
        self.assertEquals(test_df2.index.names, ['a', 'b'])

        test_df2 = test_df2.sort_index()

        test_dat3 = {'a': [10,10,10,10,11,11,11,11,12,12], 'b': np.arange(20, 30), 'c': np.arange(30, 40)}
        test_df3 = pd.DataFrame(test_dat3).set_index(['a', 'b'])
        test_df3.loc[10]
        test_df3.loc[[10]]
        test_df3.loc[[10, 11]]
        test_df3.loc[([10], [20,21]),]
        test_df3.loc[(10, 20)]
        test_df3.loc[[(10,20)]]
        type(test_df3.loc[(10, 20)])
        type(test_df3.loc[[(10, 20)]])
        test_df3.loc[pd.IndexSlice[:, [20]],]
        test_df3.loc[pd.IndexSlice[:, 20], ]     # inconsistent?  Should drop the second level in the index

