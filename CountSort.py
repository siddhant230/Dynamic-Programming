arr=[1,2,1,4,3]
arr=[2,1,6,3,7]
val=max(arr)
c=[0]*(val+1)
for i in arr:
	c[i]+=1

for j in range(1,val+1):
	c[j]=c[j]+c[j-1]
	
fin=[0]*len(arr)
for k in arr[::-1]:
	fin[c[k]-1]=k
	c[k]-=1
print(fin)