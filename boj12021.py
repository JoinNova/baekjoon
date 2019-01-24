#12021 보물찾기
a,b=map(int,input().split());i=0
while 1:
    a,b=(a+b)/2,2*a*b/(a+b)
    i+=1
    if i==100:break
print('%s %s'%(round(a,3),round(b,3)))

#02
print(2*('%f '%eval(input().replace(' ','*'))**.5))
