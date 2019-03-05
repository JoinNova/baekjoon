#boj16785ソーシャルゲーム
coupon,bonus,target=map(int, input().split());getsome=0;day=0
while 1:
    day+=1
    getsome+=coupon
    if day%7==0:
        getsome+=bonus
    if getsome>=target:
        break
print(day)

#02
c,b,t=map(int,input().split());g=d=0
while g<t:d+=1;g+=c;g=[g,g+b][d%7<1]
print(d)
