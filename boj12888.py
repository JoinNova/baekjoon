#boj12888 완전 이진 트리 도로 네트워크
'''
1 1
2 3
3 5
4 11
5 21'''
def tree(n):
    result=1
    for i in range(1,n+1):
        if i%2==0:
            result=2*result+1
        else:
            result=2*result-1
    return result
n=int(input())
print(tree(n))


#by jh05013
n = int(input())
v = 2**(n+1) - 1
print(v//3 + (1 if v%3 else 0))
