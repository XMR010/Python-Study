import math
a=float(input())
b=float(input())
c=float(input())
if a==0 and b==0:
    print("Not an equation")
elif a==0:
    x=-c/b
    print("%.2f"%x)
else:
    d=b*b-4*a*c
    if d>=0:
        d=math.sqrt(d)
        x1=(-b+d)/(2*a)
        x2=(-b-d)/(2*a)
        if x1<x2:
            x1,x2=x2,x1
        print("%.2f"%x1)
        print("%.2f"%x2)
    else:
        m=-b/(2*a)
        n=math.sqrt(-d)/abs(2*a)
        print("{:.2f}+{:.2f}i".format(m, n))
        print("{:.2f}-{:.2f}i".format(m, n))