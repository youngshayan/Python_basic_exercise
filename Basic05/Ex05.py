def triangle(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        print("yes it creates a triangle!!!")
    else:
        print("No try again!")
x=int(input('Enter a number:'))
y=int(input('Enter a number:'))
z=int(input('Enter a number:'))
triangle(x,y,z)
