#3052 나머지
s=set();exec('s.add(int(input())%42);'*10);print(len(s))
#02
print(len(set(int(input())%42 for n in range(10))))
