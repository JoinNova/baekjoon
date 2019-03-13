#boj16018 Occupy parking
a,b,c=[input()for _ in'_'*3];r=i=0;exec("r+=[0,1][b[i]==c[i]=='C'];i+=1;"*len(b));print(r)

#boj16018 Occupy parking
a,b,c=[input()for _ in'_'*3];r=0
for i in range(len(l)):
    r+=[0,1][b[i]==c[i]=='C']
print(r)
