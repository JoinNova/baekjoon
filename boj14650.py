#boj14650 걷다보니 신천역 삼

#print([0,0,2,6,18,54,162,486,1458,4374][int(input())])

n=int(input());print(0if n==1else 2*3**(n-2))

n=int(input());print([2*3**(n-2),0][n<2])
