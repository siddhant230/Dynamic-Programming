def binomial(n,k):
	arr=[[0]*(k+1) for i in range(n+1)]
	for i in range(n+1):
		for j in range(k+1):
			if j==0 or j==i:
				arr[i][j]=1
			else:
				arr[i][j]=arr[i-1][j-1]+arr[i-1][j]
	for i in arr:
		print(i)
	print(arr[n][k])
binomial(4,2)
