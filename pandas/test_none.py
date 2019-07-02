import pandas as pd

df = pd.DataFrame({'a': ["baab", "bbabbab"]})
# Chained indexing; so can expect it not to work as intended.  However works one more step of surprising.
df.a[2] = None
df     # as expected doesn't show the None
df.a   # as not expected DOES show the None.  A copy is kept in ._item_cache.
