n=int(input())
c=0
l=[100,20,10,5,1]
for i in range(5):
    c+=int(n/l[i])
    n=n%l[i]
print(c)