import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

eng_freq = {
    "a": 8.167,
    "b": 1.492,
    "c": 2.782,
    "d": 4.253,
    "e": 12.702,
    "f": 2.228,
    "g": 2.015,
    "h": 6.094,
    "i": 6.966,
    "j": 0.153,
    "k": 0.772,
    "l": 4.025,
    "m": 2.406,
    "n": 6.749,
    "o": 7.507,
    "p": 1.929,
    "q": 0.095,
    "r": 5.987,
    "s": 6.327,
    "t": 9.056,
    "u": 2.758,
    "v": 0.978,
    "w": 2.360,
    "x": 0.150,
    "y": 1.974,
    "z": 0.074}

def meas(fs):
    """Single number measure to check how close to frequencies of english

    for correct freqs get 0.065
    for uniform on letters get 0.038
    """
    return sum((f/100)**2 for f in fs)


meas(eng_freq.values())
meas([100/26 for _ in range(26)])

freqs = list(eng_freq.values())

def barplot(freqs):
    plt.bar(np.arange(len(freqs)), freqs)

barplot(freqs)

def rot_freqs(freqs, ct):
    return freqs[ct:] + freqs[:ct]

def mixin_freqs(fs, freqs, ct):
    return np.array([x + y for x, y in zip(fs, rot_freqs(freqs, ct))])


import random
fs = np.array(freqs)
idxs = []
vals = []
for i in range(200):
    vals.append(meas((100 * fs) / sum(fs)))
    idx = random.randrange(0, 26)
    idxs.append(idx)
    fs = mixin_freqs(fs, freqs, idx)
print(meas((100 * fs) / sum(fs)))

plt.plot(vals)
plt.title("Showing speed of convergence to uniform")
