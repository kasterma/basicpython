# Running some tests on wheel sampling

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def kl_divergence(ps, qs):
    return np.sum(ps * np.log2(ps / qs))


ps = np.array([0.36, 0.48, 0.16])
qs = np.ones(3)/3

indices = np.arange(len(ps))
width = 0.45
plt.bar(indices - width/2, ps, width=width, label="p")
plt.bar(indices + width/2, qs, width=width, label="q")
plt.xticks([0, 1, 2], ['0', '1', '2'])
plt.legend()
plt.title("Showing the two distributions")
plt.text(1.3, 0.45, f"$D_{{KL}}(p \\parallel q) = {kl_divergence(ps, qs):.4}$")
plt.text(1.3, 0.42, f"$D_{{KL}}(q \\parallel p) = {kl_divergence(qs, ps):.4}$")
plt.show()

kl_divergence(ps, qs)
kl_divergence(qs, ps)


def ent(ps):
    return -np.sum(ps*np.log2(ps))


def normalize(cs) -> np.array:
    """Given a sequence of weights, normalize to a distribution."""
    return np.array(cs / np.sum(cs))


ws = [0.1, 0.5, 7.7]


def select_intuitive(ws):
    cs = np.cumsum(ws)
    r = np.random.uniform(0, sum(ws))
    return np.min(np.where(cs > r))


def select_clever(ws):
    index = np.random.randint(0, len(ws))
    beta = np.random.uniform(0, 2*max(ws))  # exact with sum(ws)
    c = ws[index]
    while c < beta:
        index = (index + 1) % len(ws)
        c += ws[index]
    return index


def select_clever_sequence(ws, n, weighted_starting=True):
    indices = []
    if weighted_starting:
        index = 0
        beta = np.random.uniform(0, sum(ws))
        c = ws[index]
        while c < beta:
            index = (index + 1) % len(ws)
            c += ws[index]
    else:
        index = np.random.randint(0, len(ws))   # random starting location
    beta = ws[index]
    c = ws[index]
    for _ in range(n):
        beta += np.random.uniform(0, 2*max(ws))
        while c < beta:
            index = (index + 1) % len(ws)
            c += ws[index]
        indices.append(index)
    return indices


N = 100000
s1 = [select_intuitive(ws) for _ in range(N)]
s2 = [select_clever(ws) for _ in range(N)]
s3 = select_clever_sequence(ws, N)
s4 = select_clever_sequence(ws, N, weighted_starting=False)
d1 = pd.Series(s1).value_counts(normalize=True)
d2 = pd.Series(s2).value_counts(normalize=True)
d3 = pd.Series(s3).value_counts(normalize=True)
d4 = pd.Series(s4).value_counts(normalize=True)
print(d1)
print(d2)
print(d3)
print(d4)

d_goal = pd.Series(normalize(ws))

kl_divergence(d_goal, d1)
kl_divergence(d_goal, d2)
kl_divergence(d_goal, d3)
kl_divergence(d_goal, d4)


def collect(ws, n, k, type):
    zeros = []
    ones = []
    twos = []
    for _ in range(k):
        if type == "clever_sequence":
            s = select_clever_sequence(ws, N)
        elif type == "clever":
            s = [select_clever(ws) for _ in range(N)]
        elif type == "intuitive":
            s = [select_intuitive(ws) for _ in range(N)]
        else:
            print("invalid type")
            return None
        cs = pd.Series(s).value_counts()
        zeros.append(cs[0])
        ones.append(cs[1])
        twos.append(cs[2])
    return {1: ones, 0: zeros, 2: twos}


col1 = collect(ws, N, 100, "intuitive")
np.mean(col1[0])
np.mean(col1[1])
np.mean(col1[2])
