# Some quick tests for the effect of extra input on a hash
#
# Given some sources of entropy, show the effect of a malicious source that can read all other sources.

import hashlib
import random
import string
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KernelDensity


def random_string(length=10):
    return "".join(random.choices(string.ascii_letters, k=length))


def get_with_zeros(initial, num_zeros):
    """
    The initial value is the data containing entropy as collected for other sources.  num_zeros gives the size of the
    bias we are trying to establish.  This search is one way the malicious source of data could create that bias.

    :param initial: the initial value for this search
    :param num_zeros: fixed initial segment to search for
    :return: i such that with bytes(i) added to the digest get the right number of initial zeros
    """
    base_hash = hashlib.md5()
    base_hash.update(initial)

    data_to_add = 0
    while True:
        updated_hash = base_hash.copy()
        updated_hash.update(bytes(data_to_add))
        if all([b == 0 for b in updated_hash.digest()[0:num_zeros]]):
            break

        data_to_add += 1

        if data_to_add % 1000 == 0:
            print(data_to_add)

    return data_to_add


class Timer():
    def __init__(self):
        self.start = time.monotonic()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.monotonic()
        runtime = end - self.start
        print(f"Time taken {runtime}")



def collect_data(ct):
    return [get_with_zeros(random_string().encode(), 1) for j in range(ct)]

with Timer():
    dat = collect_data(100)

with Timer():
    collect_data(1000)

with Timer():
    collect_data(5000)

with Timer():
    collect_data(10_000)

dat = collect_data(100_000)


np.mean(dat)
np.max(dat)
np.min(dat)

with Timer():
    get_with_zeros(random_string().encode(), 1)

datn = np.array(dat)
datf = pd.DataFrame({'found': datn})
datf
datf.plot()
plt.show()

cts = datf.found.value_counts()

bins = np.histogram(cts, bins=10)


# hist of search sizes

### cts.hist()   # wrong plot, plots the cts not the indices
plt.hist(datf.values, bins=30)
m = np.mean(datf.values)
plt.axvline(x=m, color='red')
plt.show()

# kernel density approx of search sizes

kd = KernelDensity()
kd.fit(datf.values)
dd = kd.sample(10000)
plt.hist(dd, bins=30)
plt.show()
np.mean(dd)
np.std(dd)
np.std(datf.values)

xs = np.linspace(0, 3000, num=1000)
dens_dat = np.exp(kd.score_samples(np.expand_dims(xs, 1)))
plt.plot(xs, dens_dat)
plt.show()

# quick play with kernel density fn

kd2 = KernelDensity(bandwidth=0.3, kernel='tophat')
kd2.kernel
dat_train = np.expand_dims(np.asarray([1, 1, 1.5, 2, 2, 2]), 1)
kd2.fit(dat_train)
xs = np.linspace(0, 4, num=100)
ys = np.exp(kd2.score_samples(np.expand_dims(xs, 1)))
plt.plot(xs, ys)
plt.show()
