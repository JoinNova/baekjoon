#2774 아름다운수
i=input
for _ in'_'*int(i()):
 s=set()
 for _ in i():s.add(_)
 print(len(s))
#02
i=input;exec('print(len({*i()}));'*int(i()))
