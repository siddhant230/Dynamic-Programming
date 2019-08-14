def lcs(X,Y):
	row=len(X)
	cols=len(Y)
	arr=[[None]*(cols+1) for i in range(row+1)]
	print(arr)

	for i in range(row+1):
		for j in range(cols+1):
		
			if i==0 or j==0:
				print(i,j)
				arr[i][j]=0
			elif X[i-1]==Y[j-1]:
					arr[i][j]=arr[i-1][j-1]+1
			else:
				arr[i][j]=max(arr[i-1][j],arr[i][j-1])
		
	print(arr)
	req_sub=''
	k=0
	m=row
	n=cols
	for lol in arr:
		print(lol)
	while arr[m][n]!=0:
		if arr[m][n]==arr[m-1][n]:
			m=m-1
			n=n
		elif arr[m][n]==arr[m][n-1]:
			m=m
			n=n-1
		else:
			req_sub+=Y[n-1]
			m-=1
			n-=1
	val=list(reversed(req_sub))
	print('Longest Common Subsequence is =>',end=' ')
	print(''.join(val))
	print(arr[row][cols])
	
lcs(input('string 1=>').lower(),input('string2=>').lower())
