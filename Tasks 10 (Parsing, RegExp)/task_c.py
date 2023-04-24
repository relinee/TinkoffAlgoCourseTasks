import re
import sys

# s/"(word1)\s+('.+?')\s+(word3)"/"$1 $3 $2"/
# = Regex.Replace(str, @"\\circle{\((\d+),(\d+)", @"\circle{($2,$1");
#REGEX_MASK = r's/\\circle{\((\d+),(\d+)/\\circle{\($2,$1'

REGEX_MASK = r'\\circle{\((\d+),(\d+)\)'
REGEX_SUB = r'\\circle{(\2,\1)'

for line in sys.stdin:
    res = re.sub(REGEX_MASK, REGEX_SUB, line)
    print(res, end=' ')
