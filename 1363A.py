for t in range(int(input())):
	n, k = map(int, input().split())
	x = list(map(int, input().split()))

	odd = sum([i%2 for i in x])
	even = n-odd

	ans = 'No'
	for e in range(k):
		if e <= even and k-e <= odd and (k-e)%2 == 1:
			ans = 'Yes'
			break
	print(ans)