def neg(a,b):
    if a>b:
        a, b = b, a
    while a<b-1 :
        a = a + 2
        print(a)
x=int(input('Enter a number:'))
y=int(input('Enter a number:'))
(neg(x,y))
