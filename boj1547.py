#1547 공
l=[0,1,0,0];i=input;exec('a,b=map(int,i().split());l[a],l[b]=l[b],l[a];'*int(i()));print(l.index(1))

#02
l=[0,1,0,0];i=input;exec('a,b=map(int,i()[::2]);l[a],l[b]=l[b],l[a];'*int(i()));print(l.index(1))
