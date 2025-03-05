"""
Module Import Demonstration

This script demonstrates:
1. Different ways to import modules
2. Using imported functions and classes
3. Wildcard imports
4. Module aliasing
5. External library imports

Author: Shayan Mansornia
"""

# Example of module import with alias (commented out)
# import Mymodule as my
# my.hello("Shayan")
# my.sms("09108845546")
#
# name1 = my.User("Amir")
# name1.printname()

# Demonstrate wildcard import from custom module
from Mymodule import *
hello("shayan")
sms("003993939")
name1 = User("AsQAr")
name1.printname()

# Import external library
import pytz
