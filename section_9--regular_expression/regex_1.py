import re

'''regex_1.py: Pattern eggs must be the prefix of the pattern'''

pattern = r"eggs"

if re.match(pattern, "eggseggsssrggggbacon"):
    print('Match found!')
else:
    print('No match found!')
