#boj16648 Accumulator Battery
movetime,startper=map(int,input().split())
if startper>=20:
    drainperspeed=(100-startper)/movetime
    print((startper-20)/drainperspeed+20/(drainperspeed/2))
else:
    drainspeed=(80+(20-startper)*2)/movetime
    print(startper/(drainspeed/2))
