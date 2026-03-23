import random
n=int(input())
total=0
for i in range(100000):
    s=0
    while s<=50:
        s+=random.randint(1,n)
    total+=s
print(f"{total/100000:.1f}")
