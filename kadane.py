def kadane(arr):
	print(arr)
	dp=[arr[0]]
	
	for i in range(1,len(arr)):
		val=max(dp[-1]+arr[i],arr[i])
		dp.append(val)
		print(dp)
	return max(dp)

arr=[1,-3,2,1,1]		
arr=[-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7] 
#arr=[-2, -3, 4, -1, -2, 1, 5, -3]
print(kadane(arr))