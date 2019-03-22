##boj2839 설탕배달
n=int(input())
if n==4 or n==7:
    print(-1)
else:
    for i in range(5):
        if (n-3*i)%5==0:
            print(i+(n-3*i)//5)          
            break
