#  to find how many upper case and lower  case letter is in entry sentence
def count_str(sentence):
    upper_count = 0
    lower_count = 0
    for letter in sentence:
        if letter.isupper():
            upper_count += 1
        elif letter.islower():
            lower_count += 1
    print(f"Your sentence have {upper_count} upper case letter!")
    print(f"your sentence have {lower_count} lower case letter!")
while True:
    sentence = input("Enter your sentence: ")
    print("type exit to end the program")
    count_str(sentence)
    if sentence == "exit":
        break


