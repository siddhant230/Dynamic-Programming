fib={}
def fibo(n):
	if n==1:
		return 1		
	if n not in fib:
		if n<=1:
			fib[n]=n
		else:
			fib[n]=fibo(n-1)+fibo(n-2)
	return (fib[n])
print(fibo(5))
