import random
random.seed(125)
n=0
a=random.randint(0,100)
while True:
    b=input("Please input:")
    try:
        b=int(b)
    except ValueError:
        print("Please input integer!")
        continue
    n=n+1
    if b==a:
        print(f"{n} times,you got it!")
        break
    elif b<a:
        print("Too small!")
    else:
        print("Too big!")
