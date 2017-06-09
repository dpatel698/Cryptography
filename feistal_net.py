import itertools
from functools import *

def binary_strings(n):
    return [''.join(binary for binary in tup) for tup in itertools.product('01', repeat=n)]
