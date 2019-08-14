def printer(arr):
	for i in arr:
		print(i)

def longestpalin(s,i,j):
	n=len(s)
	arr=[[0 for x in range(len(s))] for i in range(len(s))]
	
	for p in range(j):
		arr[p][p]=1
	for cl in range(2,n+1):
		for i in range(n-cl+1):
			j=i+cl-1
			if s[i]==s[j] and cl==2:
				arr[i][j]=2
			elif s[i]==s[j]:
				arr[i][j]=arr[i+1][j-1]+2
			else:
				arr[i][j]=max(arr[i][j-1],arr[i+1][j])
	printer(arr)
	return arr[0][n-1]	
	
s='geeks for geeks'

print(longestpalin(s,0,len(s)))
