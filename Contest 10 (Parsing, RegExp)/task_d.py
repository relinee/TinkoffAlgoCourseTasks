import re
import sys

REGEX_MASK1 = r'\$v_(\d)\$'
REGEX_MASK2 = r'\$v_\{(.+)\}\$'
REGEX_MASK3 = r'\$v_(.)\$'
REGEX_SUB = r'v[\1]'

for line in sys.stdin:
    res = re.sub(REGEX_MASK1, REGEX_SUB, line)
    res = re.sub(REGEX_MASK2, REGEX_SUB, res)
    res = re.sub(REGEX_MASK3, REGEX_SUB, res)
    print(res, end=' ')