#9658 돌 게임
s='SK';c='CY';print([s,c,s,c,s,s,s][int(input())%7])
#02
l='13';print('CY'if l.count(str(int(input())%7))else'SK')

print('CY'if int(input())%7 in [1,3] else'SK')
