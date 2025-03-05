"""
Python Standard and Third-Party Library Usage

This script demonstrates:
1. Platform information retrieval
2. Random number generation
3. Date and time manipulation
4. Timezone handling
5. Various Python library imports

Author: Shayan Mansornia
"""

# Import required libraries
import platform
import random
from datetime import *
import pytz

# Get system information
print(platform.system())

# Generate random number
print(random.randint(10, 1231313))

# Get current date and time
x = datetime.now()
print(x)

# Calculate future date
start = datetime.now()
end = start + timedelta(days=30)
print(end)

# Access timezone information
print(pytz.HOUR)