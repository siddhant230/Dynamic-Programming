n=int(input('enter '))
fact=[]
for i in range(1,n+1):
	if i==1:
		fact.append(i)
	else:
		fact.append(i*fact[-1])
print(fact)
print(fact[n-1])