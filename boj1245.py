#boj1145 거의대부분의배수
from itertools import combinations as c
import math    
def lcm(a, b):return a * b // math.gcd(a, b)
l=[*map(int,input().split())];result=1000000
for _ in c(l,3):
    result=min(result,lcm(_[0],lcm(_[1],_[2])))
print(result)
