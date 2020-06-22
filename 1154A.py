l=[0,0,0,0]
l[0],l[1],l[2],l[3]=map(int,input().split())
z=max(l)
l.remove(z)
print(z-l[0],z-l[1],z-l[2],end='')