#1062 가르침
#anta +' ' + tica   #antic
# abcdefghijklmnopqrstuvwxyz
'''
n,k=map(int,input().split())

for i in range(n):
    t=input()[4:-4]
    print(t)
'''

n,k = map(int,input().split())
word = []
count = 0
max_count = 0
redundancy = 0
flag = True
for i in range(n):
    ##입력받은 단어를 집합으로 필터링하고 리스트로 정렬
    temp = sorted(list(set(input())))
    if len(temp) <= k:
        ##리스트를 문자열로 변환하고 단어리스트에 추가
        temp = ''.join(temp)
        word.append(temp)
if k >= 5:
    for i in range(len(word)):
        redundancy = k - len(word[i])
        #전체비교를 할 때 나한테 없는 알파벳이 나왔을때 
        #내가 몇개를 더 배울수 있는지 확인하는 변수
        for j in range(len(word)):
            for u in word[j]:
                if u in word[i]:
                    #word[j]에 저장된 알파벳들이 word[i]에도 있는지 각각 확인
                    pass
                else:
                    #없는 글자라면 내가 더 배울수 있는지 확인 후 종료여부 결정
                    if redundancy > 0:
                        redundancy -= 1
                    else:
                        flag = False
                        break
            if flag:
                #전체비교했을때 모든글자가 다 있거나 더 배울수 있어서 for문을 통과한경우
                count += 1
            flag = True
        if max_count < count:
            max_count = count
        count = 0
    print(max_count)
else:
    print(0)
