t=input();jum,sharp,star='.','#','*'
line1=''
line2=''
line3=''
chk=0
for i in range(len(t)):
    if (i+1)%3!=0:
        line1+=jum*2+sharp+jum
        line2+=jum+sharp+jum+sharp
        if i%3==0 and i!=0:
            line3+=star+jum+t[i]+jum
        else:
            line3+=sharp+jum+t[i]+jum
    else:
        line1+=jum*2+star+jum
        line2+=jum+star+jum+star
        line3+=star+jum+t[i]+jum
line1+=jum
line2+=jum
line3+=[star,sharp][len(t)%3>0]
print(line1)
print(line2)
print(line3)
print(line2)
print(line1)

#02
t=input();x,y,z='.','#','*';a=b=c=''
for i in range(len(t)):
 if (i+1)%3!=0:a+='..#.';b+='.#.#';c+=[y,z][i%3==0 and i!=0]+x+t[i]+x
 else:a+='..*.';b+='.*.*';c+=z+x+t[i]+x
a+=x;b+=x;c+=[z,y][len(t)%3>0];print(a,b,c,b,a,sep='\n')
