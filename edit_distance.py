def edit_distance(x,y):
	row=len(x)+1
	cols=len(y)+1	
	arr=[[0]*cols for i in range(row)]
	
	for i in range(row):
		for j in range(cols):
			if i==0:
				arr[i][j]=j
			elif j==0:
				arr[i][j]=i
				
			elif x[i-1]==y[j-1]:	
				arr[i][j]=arr[i-1][j-1]
			else:
				arr[i][j]=1+min(arr[i-1][j-1],arr[i][j-1],arr[i-1][j])
			
	print(arr[row-1][cols-1])

edit_distance('cart','march')