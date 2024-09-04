number1 = int(input("\nEnter a number between 1 and 9 ----> "))
if 1 <= number1 <= 9:
    number = number1 * 2
    number += 8
    number += number1
    number -= 2
    number /= 3
    number -= number1
    number *= 4
    number = int(number)
    print(f'\nYour final answer must be 8 and it is ----> {number} \n')
else:
    print("The number you've entered isn't between 1 and 9.") 
# small game
