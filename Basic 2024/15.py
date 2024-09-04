def calc(number):
    if number % 2 == 0:
        print("Number is ---> even")
    else:
        print("Number is ---> odd")
while True:
    print("type exit to close the program!!")
    number = int(input("\nEnter your number: "))
    calc(number)
    if number == "exit":
        break
