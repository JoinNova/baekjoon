#10823 더하기2
import sys;print(eval(sys.stdin.read().replace('\n','').replace(',','+')))
#02 by sait2000
s=''
try:
 while 1:s+=input()
except:print(sum(eval(s)))
