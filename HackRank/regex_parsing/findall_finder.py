"""Findall and finder"""

import re
pattern = r'(?<=[^aeiouAEIOU])([aeiouAEIOU]{2,})(?=[^aeiouAEIOU])'
matches = re.findall(pattern, input())
print('\n'.join(matches) if matches else -1)
