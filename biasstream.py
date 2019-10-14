# generate a stream with bias, see how can use that in a one time pad

import string
import random

from collections import Counter


def one_letter_less(letter, f):
    d = {l: 1/26 + (1/26 - f)/25 for l in string.ascii_lowercase}
    d[letter] = f
    return d


d_even = {l: 1/26 for l in string.ascii_lowercase}
d_qless = one_letter_less("q", 1/100)


def gen_seq(d, l):
    return random.choices(list(d.keys()), list(d.values()), k=l)


def apply(m, k):
    return [chr(((ord(i) - ord('a') + ord(j) - ord('a')) % 26) + ord('a')) for i, j in zip(m, k)]


def inv_apply(m, k):
    return [chr(((ord(i) - ord('a') - (ord(j) - ord('a'))) % 26) + ord('a')) for i, j in zip(m, k)]


k1 = gen_seq(d_qless, 10_000)
m1 = gen_seq(d_even, 10_000)
m2 = gen_seq(d_even, 10_000)
c = apply(random.choice([m1, m2]), k1)
print(Counter(k1))

print(Counter(inv_apply(c, m1)))
print(Counter(inv_apply(c, m2)))

# two texts from project Gutenberg (just wanted two large English texts)
text1 = [l.lower() for l in open("data/PridePrejudice.txt").read() if l in string.ascii_letters]
text2 = [l.lower() for l in open("data/Frankenstein.txt").read() if l in string.ascii_letters]

f1 = {l: v/len(text1) for l, v in Counter(text1).items()}
f2 = {l: v/len(text2) for l, v in Counter(text2).items()}
diff = {l: f1[l] - f2[l] for l in string.ascii_lowercase}
max(abs(v) for v in diff.values())

t1 = text1[:10_000]
t2 = text2[:10_000]
c = apply(random.choice([t1, t2]), k1)
print(Counter(inv_apply(c, t1)))
print(Counter(inv_apply(c, t2)))
inv_apply(c, k1)
