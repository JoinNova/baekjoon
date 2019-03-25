###출력 형식이 잘못되었습니다
from sys import stdin
from re import sub
n=int(stdin.readline().strip())
for i in range(n):
    a=stdin.readline().strip().lower()
    b=stdin.readline().strip().lower()
    for j in range(max(a.count(' '),b.count(''))):
        a=sub(r'[ ]{2}?',' ',a)
        b=sub(r'[ ]{2}?',' ',b)
    a=sub(r'[{]','(',a)
    b=sub(r'[{]','(',b)
    a=sub(r'[}]',')',a)
    b=sub(r'[}]',')',b)
    a=sub(r'[[]','(',a)
    b=sub(r'[[]','(',b)
    a=sub(r'[]]',')',a)
    b=sub(r'[]]',')',b)
    a=sub(r'[;]',',',a)
    b=sub(r'[;]',',',b)
    a=sub(r'[:]{1} ',':',a)
    b=sub(r'[:]{1} ',':',b)
    a=sub(r' [:]{1}',':',a)
    b=sub(r' [:]{1}',':',b)
    a=sub(r'[,]{1} ',',',a)
    b=sub(r'[,]{1} ',',',b)
    a=sub(r' [,]{1}',',',a)
    b=sub(r' [,]{1}',',',b)
    a=sub(r'[.]{1} ','.',a)
    b=sub(r'[.]{1} ','.',b)
    a=sub(r' [.]{1}','.',a)
    b=sub(r' [.]{1}','.',b)
    a=sub(r'[(]{1} ','(',a)
    b=sub(r'[(]{1} ','(',b)
    a=sub(r' [)]{1}',')',a)
    b=sub(r' [)]{1}',')',b)
    a=sub(r'[(]{1} ','(',a)
    b=sub(r'[(]{1} ','(',b)
    a=sub(r' [)]{1}',')',a)
    b=sub(r' [)]{1}',')',b)

    
    #print(a)
    #print(b)

    if i!=n-1:
        if a==b:
            print('Data Set {}: equal\n'.format(i+1))
        else:
            print('Data Set {}: not equal\n'.format(i+1))
    else:
        if a==b:
            print('Data Set {}: equal'.format(i+1))
        else:
            print('Data Set {}: not equal'.format(i+1))
