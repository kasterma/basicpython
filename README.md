# basicpython

## pandas

- loc and iloc
- SettingWithCopy
- set_index
- pd.IndexSlice

In creating functions for pd.DataFrame.pipe, start with a copy of the DataFrame.

- df.where(lambda df: df % 3 == 0, -df-2)   # note the callable that computes where to replace


- assign (0.16.0): For adding new columns to a DataFrame in a chain (inspired by dplyr's mutate)
- pipe (0.16.2): For including user-defined methods in method chains.
- rename (0.18.0): For altering axis names (in additional to changing the actual labels as before).
- Window methods (0.18): Took the top-level pd.rolling_* and pd.expanding_* functions and made them NDFrame methods with a groupby-like API.
- Resample (0.18.0) Added a new groupby-like API
- .where/mask/Indexers accept Callables (0.18.1): In the next release you'll be able to pass a callable to the indexing methods, to be evaluated within the DataFrame's context (like .query, but with code instead of strings).


- pd.DataFrame.equals, for comparing data frames (having NaN in the same place compares as true)

- [dropna](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.dropna.html)

- index operations: & intersection, | union, and ^ symmetric difference

## logging

logging.basicConfig needs to come before first call that uses it.  Otherwise will be ignored.

logging.basicConfig(level=logging.INFO)

## Misc

Use PyYaml through import yaml.

Printing without having {c: 4} as value of b:

    yaml.dump({'a': {'b': {'c' :4}}}, default_flow_style=False)

Reading a yaml file

    with open("logging_1.yaml") as f:
        dd = yaml.load(f)

Use yaml.load_all if the input contains multiple yaml documents separated by ---

Note can deal with Pythhon objects (writing and reading through tags)


## References

- [Modern Pandas (Part 1), Tom Augspurger](http://tomaugspurger.github.io/modern-1.html)
- [Modern Pandas (Part 2): Method Chaining](http://tomaugspurger.github.io/method-chaining.html)
- [pandas: View vs Copy](http://pandas-docs.github.io/pandas-docs-travis/indexing.html?highlight=view#indexing-view-versus-copy)
- [Logging Howto](https://docs.python.org/3.6/howto/logging.html)
- [3.6/library/logging](https://docs.python.org/3.6/library/logging.html)