"""
Case Counter

This script demonstrates:
1. String case analysis
2. Character counting
3. String methods (isupper, islower)
4. Program exit condition

Author: Shayan Mansornia
"""

#  to find how many upper case and lower  case letter is in entry sentence
def count_str(sentence):
    """
    Count the number of uppercase and lowercase letters in a sentence.
    
    Args:
        sentence (str): The input sentence to analyze
    """
    # Initialize counters
    upper_count = 0
    lower_count = 0
    
    # Count uppercase and lowercase letters
    for letter in sentence:
        if letter.isupper():
            upper_count += 1
        elif letter.islower():
            lower_count += 1
            
    # Display results
    print(f"Your sentence have {upper_count} upper case letter!")
    print(f"your sentence have {lower_count} lower case letter!")

# Main program loop
while True:
    sentence = input("Enter your sentence: ")
    print("type exit to end the program")
    count_str(sentence)
    if sentence == "exit":
        break


