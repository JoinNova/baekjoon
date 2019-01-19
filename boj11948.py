#11948 과목선택
i=input;t=int;print(sum(sorted(t(i())for _ in'_'*4)[1:])+max(t(i()),t(i())))
#02
l=[int(input())for _ in'_'*6];print(sum(sorted(l[:4])[1:])+max(l[4:]))

#03 by sait2000
x=lambda n:sorted(int(input())for i in'_'*n)[1:];print(sum(x(4)+x(2)))

#04 by Istar
d=[*eval("int(input()),"*6)];print(sum(sorted(d[:4])[1:])+max(d[4:]))
