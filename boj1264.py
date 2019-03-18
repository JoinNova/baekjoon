#boj1264 모음의개수
import re
txt=input()
while txt!='#':
    convert=len(re.sub(r'[aeiouAEIOU]','',txt))
    print(len(txt)-convert)
    txt=input()


t=input()
while'#'!=t:print(sum([t.count(x)for x in'aeiouAEIOU']));t=input()


#by sait2000
s=input()
while'#'!=s:print(sum(map(s.lower().count,'aeiou')));s=input()

#by skygarlics
S=input()
while S!='#':print(sum(i in'aeiou'for i in S.lower()));S=input()
