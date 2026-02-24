"""Re.split"""

import re

REGEX = r"[,.]"
print("\n".join(re.split(REGEX, input())))
