#boj14651 걷다보니 신천역 삼 (Large)
n=int(input());print(0if n==1else 2*3**(n-2)%1000000009)

n=int(input());print([2*3**(n-2)%1000000009,0][n<2])
