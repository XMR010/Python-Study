n=int(input())
count=0
total=20**5
for a in range(1,21):
    for b in range(1,21):
        for c in range(1,21):
            for d in range(1,21):
                for e in range(1,21):
                    if a+b+c+d+e==n:
                        count+=1
print("%.2f"%(count/total))
