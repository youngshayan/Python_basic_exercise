"""
HTTP Request and Variable Manipulation Example

This script demonstrates various Python concepts including:
1. Variable declaration and f-string formatting
2. List manipulation using insert()
3. Making HTTP requests using the requests library
4. Working with HTTP response objects

Author: Shayan Mansornia
"""

# Demonstrate variable declaration and f-string formatting
variable = 5
print(f"{variable = }")  # Prints "variable = 5" using f-string

# Demonstrate list manipulation
myList = [10, 20]
myList.insert(0, 15)  # Insert 15 at index 0
print(myList)  # Output: [15, 10, 20]

# Import the requests library for HTTP operations
import requests

# Making a HEAD request to httpbin.org
# HEAD requests are similar to GET requests but don't return the response body
r = requests.head('https://httpbin.org/', data={'key': 'value'})

# Check the status code of the response
# 200 indicates successful request
print(r)  # Prints the response object

# Print the response headers
# Headers contain metadata about the response
print(r.headers)

# Check the response content
# Note: HEAD requests typically don't return content
print(r.content)
