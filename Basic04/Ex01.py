#program to find largest number out of 10 number
maxx=int(input('Enter a number:'))
for i in range(9):
      a=int(input('Enter a number:'))
      if a > maxx:
        maxx=a
print('largest number is:',maxx)