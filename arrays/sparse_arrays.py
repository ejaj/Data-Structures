import math
import os
import random
import re
import sys
from collections import Counter

def matchingStrings(strings, queries):
    s = Counter(strings)
    result = []

    for q in queries:
        result.append(s[q])

    return result
