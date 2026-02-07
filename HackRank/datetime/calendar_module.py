""""Calendar Module"""

import calendar
from datetime import datetime

date = datetime.strptime(input(), '%m %d %Y').weekday()
print(calendar.day_name[date].upper())
