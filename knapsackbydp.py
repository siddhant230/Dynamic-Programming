def knapbydp(wt,val,cap):
	arr=[[0]*(cap+1) for i in range(len(val)+1)]
	
	for i in range(len(val)+1):
		for j in range(cap+1):
			if i==0 or j==0:
				arr[i][j]=0			
			elif wt[i-1]<=j:
				arr[i][j]=max(val[i-1]+arr[i-1][j-wt[i-1]] , arr[i-1][j])
			else:
				arr[i][j]=arr[i-1][j]

	print(arr[len(val)][cap])


wt=[10,20,30]
val=[60,100,120]
cap=30
knapbydp(wt,val,cap)