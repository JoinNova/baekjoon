#boj10768 특별한 날
a='After';b='Before';m=int(input());d=int(input());
print([[[['Special',b][d<18],a][d>18],b][m<2],a][m>2])
