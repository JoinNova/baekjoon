#2751 수 정렬하기2 pypy3
import sys
def merge(x):
    if len(x)>1:#조건바꿈
        mid=len(x)//2
        left=x[:mid]
        right=x[mid:]
        merge(left)
        merge(right)#함수 합침

    #return merge(leftl,rightl)
#def merge(left,right):
        lidx=0
        ridx=0
        chk=0
        while len(left)>lidx and len(right)>ridx:#조건변경 or -> and
            #if len(left)>0 and len(right)>0:
            if left[lidx]<right[ridx]:
                x[chk]=left[lidx]
                #righ=right[1:]
                lidx+=1
            else:#조건변경 elif -> else
                x[chk]=right[ridx]#r.append(left[0])
                #left=left[1:]
                ridx+=1
            chk+=1
            
        while lidx<len(left):
            x[chk]=left[lidx]
            lidx+=1
            chk+=1
        while ridx<len(right):
            x[chk]=right[ridx]
            ridx+=1
            chk+=1
    return l
'''
        elif len(left)>0:
            r.append(left[0])
            left=left[1:]
        elif len(right)>0:
            r.append(right[0])
            right=right[1:]
    return r
'''
s=sys.stdin.readline
n=int(s());l=[]
for _ in'_'*n:num=int(s());l.append(num)
#    if num not in lst:      #중복이 없다고했으니 제거
print(*merge(l),sep='\n')


#02 python3
import sys;i=sys.stdin.readline;print(*sorted(int(i())for _ in'_'*int(i())),sep='\n')

#03 pypy3
i=input;print(*sorted(int(i())for _ in'_'*int(i())),sep='\n')

