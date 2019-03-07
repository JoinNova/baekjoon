#boj1620 나는야 포켓몬 마스터 이다솜
import sys;s=sys.stdin.readline
n,m=map(int,s().split())
dic={};numberdic={}
for i in range(n):
    pokemon=s().strip()
    dic[i]=pokemon
    numberdic[pokemon]=i
for _ in'_'*m:
    quiz=s().strip()
    if quiz.isnumeric():
        print(dic[int(quiz)-1])
    else:
        print(numberdic[quiz]+1)
