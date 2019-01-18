#9325 얼마?
i=input;t=int
for _ in'_'*t(i()):r=0;r+=t(i());exec('r+=eval(i().replace(" ","*"));'*t(i()));print(r)

#02
i=input;t=int;exec("r=t(i());exec('a,b=map(t,i().split());r+=a*b;'*t(i()));print(r);"*t(i()))
