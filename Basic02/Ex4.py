a=int(input('Enter a:'))
b=int(input('Enter b:'))
if a>b:
    a,b=b,a
    print('a:',b)
    print('b:',a)
else:
    print('again')
