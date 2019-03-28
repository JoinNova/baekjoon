#boj16649 Building a Stair
def stair(cube):
    cnt=cube
    row=(cube+1)//2
    print(row+1)
    pic='.'*(row+1)+'\n'
    for i in range(row):
        for j in range(row):
            if j==0 or i==row-1:
                pic+='o';cnt-=1
            elif cube%2==0 and i==row-2 and j==1:
                pic+='o';cnt-=1;
            else:
                pic+='.'
        pic+='.\n'
    print(pic.strip())
    #print(cnt)
n=int(input())
if n==2:print(-1)
else:stair(n)
