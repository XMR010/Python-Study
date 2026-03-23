for n in range(100, 301):
    a=0
    for d in range(2,int(n**0.5)+1):
        if n%d==0:
            a=1
            break
    if a==0:  
        print(n,end=" ")