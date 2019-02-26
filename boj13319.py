$boj13319 가짜소수 TEXT
2152302898747 6763
#02
3474749660383 1303


#413138881 617
#1299963601 601
#1207252621 613
#5816382001 521
#2301745249 727
#71171308081 6841
#11346205609 1237
#1644945775201 547
#464052305161 4261
#3474749660383 1303
#959377262271049 54277

'''
import sys
sys.setrecursionlimit(1500000)
def mul( n, m, M) :
    if m :
        return 0
    if m %2 == 1 :
        return (n + mul( n * 2 % M , m // 2, M )) % M
    else : return mul( n * 2 % M, m // 2, M )

def pw( n, m, M ):
    ans = 1
    while m:
        if m % 2 == 1 :
            ans = mul( ans, n, M )
        n = mul( n, n, M )
        m >>= 1
    return ans
            

if __name__ == "__main__":
    n,m=map(int, input().split())
    for i in range(2,3):
        print( pw( i, n-1, n ))
'''
