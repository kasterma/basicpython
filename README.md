# basicpython

## pandas

- loc and iloc
- SettingWithCopy
- set_index
- pd.IndexSlice

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
- [pandas: View vs Copy](http://pandas-docs.github.io/pandas-docs-travis/indexing.html?highlight=view#indexing-view-versus-copy)
- [Logging Howto](https://docs.python.org/3.6/howto/logging.html)
- [3.6/library/logging](https://docs.python.org/3.6/library/logging.html)