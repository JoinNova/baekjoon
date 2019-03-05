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
