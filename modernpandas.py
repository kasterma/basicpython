# Notes on http://tomaugspurger.github.io/modern-1.html

# imports as from page

import zipfile

import requests
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import unittest
import tempfile
import os
import logging
import logging.config
import yaml

from functools import wraps
import re

LOG_CONF_FILENAME = "logging_modernpandas.yaml"
with open(LOG_CONF_FILENAME) as log_conf_file:
    log_conf = yaml.load(log_conf_file)
logging.config.dictConfig(log_conf)


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


class ChainingExample:
    """Generate some test data for playing with chaining of methods"""
    def __init__(self):
        self.log = logging.getLogger(self.__class__.__name__)

    def __enter__(self):
        self.fd, self.filename = tempfile.mkstemp()
        self.log.info("Creating csv file: %s", self.filename)
        dat = {'a': np.arange(20), 'b': np.arange(20, 40), 'date': pd.date_range("20170101", "20170120")}
        df = pd.DataFrame(dat, index=pd.Index(np.arange(40,60), name="idx1"))
        ff = os.fdopen(self.fd, "w")
        df.to_csv(ff)
        ff.close()
        return self.filename

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.remove(self.filename)
        return True


def log_shape(log: logging.Logger, level: int = logging.DEBUG):
    """Create wrapper function of logging the shapes of (first) input and output of a function.
    
    The log output resembles a type specification of the function
    
        f: (20, 3) -> (20, 3)
    """
    def decor(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            log.log(level, "%s: %s -> %s" % (func.__name__, args[0].shape, result.shape))
            return result
        return wrapper
    return decor


def log_dtypes(log: logging.Logger, level: int = logging.DEBUG, *, full: bool =True):
    """Create wrapper function for logging the dtypes of a function.
    
    If full is True give a log output resembling a type of the function
    
        f: (a : int64, b : int64, date : object) -> (a : int64, b : int64, date : datetime64[ns])
        
    otherwise give the name of the function and the repr of df.dtypes of the output.
    
        f, a                int64
        b                int64
        date    datetime64[ns]
        dtype: object
    """
    def rep_dtypes(df):
        """Cleaner string representation of the dtypes of a dataframe for logging"""
        return "(" + re.sub(", dtype.*", "", re.sub(r"  +", ": ", str(df.dtypes)).replace("\n", ", ")) + ")"

    def decor(func):
        if full:
            @wraps(func)
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                log.log(level, "%s: %s -> %s" % (func.__name__, rep_dtypes(args[0]), rep_dtypes(result)))
                return result
        else:
            @wraps(func)
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                log.log(level, "%s, %s" % (func.__name__, result.dtypes))
                return result
        return wrapper
    return decor


class ChainingTests(unittest.TestCase):
    log = logging.getLogger("ChainingTests")

    def test_where_callable(self):
        df = pd.DataFrame(np.arange(10).reshape(-1, 2), columns=['A', 'B'])
        m = df % 3 == 0
        df2 = df.where(m, -df-2)
        df3 = df.where(lambda df: df % 3 == 0, -df-2)
        self.assertTrue(all(df2 == df3))

    def test_chain1(self):
        with ChainingExample() as csv_filename:
            df1 = pd.read_csv(csv_filename).set_index(['idx1'])

        self.assertEquals(df1.dtypes['date'], np.dtype("O"))

        @log_shape(self.log)
        @log_dtypes(self.log, full=False)
        @log_dtypes(self.log)
        def date_to_date(df: pd.DataFrame, col):
            df_rv = df.copy()
            df_rv[col] = pd.to_datetime(df[col])
            return df_rv

        df2 = df1.pipe(date_to_date, 'date')

        # check state before to check date_to_date didn't change
        self.assertEquals(df1.dtypes['date'], np.dtype("O"))

        self.assertEquals(df2.dtypes['date'], np.dtype('<M8[ns]'))
        self.assertEquals(df2.date.dtype, np.dtype('<M8[ns]'))
        self.assertEquals(df1.shape, df2.shape)

    def test_chain_fn(self):
        """Exercise all fn in the daily flight pattern example"""
        df1 = pd.DataFrame({'a': [1, 2, np.NaN], 'b': ["hi", np.NaN, "ho"]})
        onlyA = df1.dropna(subset=[1], axis=1)

        comp: pd.DataFrame = onlyA.loc[0:1] == [1, 2]   # helps with the mistaking type error highlighting in pycharm
        self.assertTrue(all(comp))
        self.assertTrue(all(np.isnan(onlyA.loc[2])))

        self.assertTrue(pd.DataFrame({'a': [1.0], 'b': ['hi']}).equals(df1.dropna()))

        df2 = pd.DataFrame({'a': [1, 2, np.NaN, np.NaN], 'b': ["hi", None, "ho", None]})
        self.assertTrue(df1.equals(df2.dropna(how='all')))

        df2.fillna(-1)
        # both columns have two NaN
        self.assertEquals((df2.fillna(-1) == -1.0).a.value_counts()[True], 2)
        self.assertEquals((df2.fillna(-1) == -1.0).b.value_counts()[True], 2)
        self.assertTrue(pd.Series([2, 2], index=['a', 'b']).equals(df2.isnull().sum()))

        df2.a.map(np.isnan).value_counts()[True]  # replaced by isnull().sum() above, and only works for numeric cols

        df2.apply(lambda row: row.isnull().sum(), axis=1)  # count of missing values per row
        df2.apply(lambda col: col.isnull().sum())          # count of missing values per column
        df2.isnull().sum(axis=1)  # count of missing values per row
        df2.isnull().sum(axis=0)  # count of missing values per column

        comp2: np.ndarray = df2.isin([1.0, 2, "ho"]).values.sum(axis=0) == [2, 1]
        self.assertTrue(all(comp2))

        df3 = pd.DataFrame({'a': [1, 1, 2, 2], 'b': [1, 2, 3, 4]})

        df_a_sb = df3.groupby('a').b.sum()
        self.assertTrue(df_a_sb.equals(pd.Series([3,7], index=[1, 2])))   # names ignored in comparison
        pd.Series([3, 7], index=pd.Series([1, 2], name='a'), name='b')    # but can set the names if needed

        df4 = pd.DataFrame({'a': [1, 2, 3, 4], 'b': [11, 22, 33, 44]},
                           index=pd.MultiIndex.from_product([[1,2], ['aa', 'bb']], names=['idx1', 'idx2']))
        df4.columns = pd.Series(['a', 'b'], name="idx_c")
        df4.unstack(0)
        df4.unstack(1)

        df5 = pd.DataFrame([[1, 3], [2, 4], [11, 33], [22, 44]],
                           columns=pd.Series([1, 2], name="idx1"),
                           index=pd.MultiIndex.from_product([['a', 'b'], ['aa','bb']], names=['idx_c', 'idx2'])).T
        self.assertTrue(df5.equals(df4.unstack(1)))
        self.assertTrue(str(df5) == str(df4.unstack(1)))

        df5.stack(0)

        df6 = pd.DataFrame({'x': np.arange(100),
                            'y': np.concatenate([np.repeat(1, 50), np.repeat(2, 50)]),
                            'dat': pd.date_range("20170101", periods=100, freq='min')})
        df6 = df6.set_index('dat')
        df6.groupby([pd.TimeGrouper('H')]).sum()
        df7 = df6.groupby(['y', pd.TimeGrouper('H')]).sum()

        df6.x.rolling(10).sum()
