#4470 줄번호
i=1;exec('print("%d."%i,input());i+=1;'*int(input()))
#02
[print("%d."%-~i,input())for i in range(int(input()))]
#03
for i in range(int(input())):print('%d.'%(i+1),input())
