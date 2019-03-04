# Test of %run in ipython
#
# %run test_run.py
# %timeit %run test_run.py
# %run -i test_run.py  (with the environment of the current shell)
#   e.g. below we first try to double x_tr, but if not defined we set it to be the double of 3.  On next run
#   with -i we'll double the value so far


def f_tr(x: int) -> int:
    """
    Multiply by two.
    """
    return 2 * x

try:
    x_tr = f_tr(x_tr)
except NameError as e:
    print(str(e))
    x_tr = f_tr(3)
