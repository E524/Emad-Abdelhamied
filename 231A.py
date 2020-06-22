n=int(input())
c=0
l=[0,0,0]
while n>0:
	l[0],l[1],l[2]=map(int,input().split())
	if all(l) or (l[0] and l[1])==1 or (l[0] and l[2])==1 or (l[2] and l[1])==1:
		c+=1
	n-=1
print(c)