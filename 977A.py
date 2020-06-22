num,n = map(int, input().split())
while(n):
    if num%10==0:
        num=num/10
    else:
        num-=1
    n-=1
print(int(num))