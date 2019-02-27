n=int(input());result=0
for _ in range(1,n+1):
    if n%_==0:
        result+=_
print(result*5-24)
