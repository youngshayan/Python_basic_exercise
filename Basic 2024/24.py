import platform
import random
from datetime import *
import pytz
print(platform.system())
print(random.randint(10, 1231313))
x = datetime.now()
print(x)
start = datetime.now()
end = start + timedelta(days=30)
print(end)
print(pytz.HOUR)