n=int(input())
l=[]
for i in range(n):
    x,y=map(int,input().split())
    l.append((min(max(x*2,y),max(x,y*2)))**2)
for i in l:
    print(i)