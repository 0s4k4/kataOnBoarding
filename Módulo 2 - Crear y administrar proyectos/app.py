from datetime import *
from dateutil.relativedelta import *

now = datetime.now()
print(now)

now = now + relativedelta(month=1, weeks=1, hour=20)

print(now)