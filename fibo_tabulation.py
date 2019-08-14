fib=[0,1]
def fibo(n):
	for i in range(1,n):
		fib.append(fib[i]+fib[i-1])
		print(fib)
	return fib[n]
print(fibo(8))