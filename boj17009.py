#boj17009 Winning Score
f=lambda:sum(int(input())*(3-i)for i in range(3));a,b=f(),f();print(['TA'[a>b],'B'][a<b])
