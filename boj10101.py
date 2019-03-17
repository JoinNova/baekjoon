#boj10101 삼각형외우기
i=input;t=int;a,b,c=t(i()),t(i()),t(i())
print([[['Scalene','Isosceles'][a==b or b==c or c==a],'Equilateral'][a==b==c],'Error'][a+b+c!=180])
