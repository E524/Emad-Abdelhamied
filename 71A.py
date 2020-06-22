n=int(input())
l=[]
while(n>0):
	s=input()
	if len(s)>10:
		s=f'{s[0]}{len(s)-2}{s[len(s)-1]}'
	print(s)
	n-=1