#boj10102 개표
n=int(input());v=input().count('A');print([['Tie','A'][n/2<v],'B'][n/2>v])
