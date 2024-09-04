#  to find the count of each character in string we put
value = input("Enter your sentence: ")
value = value.lower()
value = value.replace(" ", "")  # to remove all the white spaces
list1 = []
for x in value:
    if x not in list1:  # to stop checking the same character in a sentence more than 1 time
        print(f"your sentence has {value.count(x)} : '{x}'")
        list1.append(x)
