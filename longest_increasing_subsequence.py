def lis(arr):
	n=len(arr)
	lis=[1]*n
	for i in range(1,n):
		for j in range(0,i+1):
			if arr[i]>arr[j]:
				lis[i]=max(lis[i],lis[j]+1)
			print(lis)
	return max(lis)
print(lis([1,3,5,2,7,1,0,8,9]))
print(lis([1,1,1]))
print(lis([1,3,5,1,2]))