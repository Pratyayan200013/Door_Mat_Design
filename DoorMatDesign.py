
l=input('n and m: ').split(' ')
n=int(l[0])
m=int(l[1])
def pattern(n,m):
    a=n//2
    b='.|.'
    for i in range(a):
        if i==0:
            print(b.center(m,'-'))
        else:
            b=b.center(len(b)+2,'.')
            b=b.center(len(b)+2,'|')
            b=b.center(len(b)+2,'.')
            print(b.center(m,'-'))
    c='WELCOME'
    print(c.center(m,'-'))
    d=b
    for i in range(a+2,n+1):
        if i==a+2:
            print(b.center(m, '-'))
        else:
            d=d[1:-1]
            d=d[1:-1]
            d=d[1:-1]
            print(d.center(m,'-'))
pattern(n,m)