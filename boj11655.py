#11655 ROT13
#ord('A')65#ord('Z')90#ord('a')97#ord('z')122#ord(' ')32#ord('N')78#ord('n')110

for _ in input():
 a=ord(_)
 if a>109:a-=13
 elif a>96:a+=13
 elif a>77:a-=13
 elif a>64:a+=13
 print(chr(a),end='')

#02
import codecs;print(codecs.encode(input(),"rot-13"))
#03
print(__import__('codecs').encode(input(),"rot13"))
