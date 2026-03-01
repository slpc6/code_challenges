"""Regex Subtitution"""

import re

PATTERN = r'(?<= )(&&|\|\|)(?= )'
for i in range(int(input())):
    string = input()
    print(re.sub(PATTERN, lambda x: 'and' if x.group() == '&&' else 'or', string))
