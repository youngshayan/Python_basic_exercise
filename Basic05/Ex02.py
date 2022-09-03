def count(a):
    c=0
    while a!=0:
        a=a//10
        c=c+1
    print(c)

x=int(input('Enter a number:'))
(count(x))