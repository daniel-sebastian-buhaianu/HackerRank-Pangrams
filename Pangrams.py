#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    char_count = Counter(s.lower())
    unique_letters = {char for char in char_count if 'a' <= char <= 'z'}
    return 'pangram' if len(unique_letters) == 26 else 'not pangram'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
