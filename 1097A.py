s=input()
li=list(input().split(' '))
for i in li:
    if s[0]==i[0] or s[1]==i[1]:
        print('Yes')
        break
    elif i==li[-1]:
        print('No')