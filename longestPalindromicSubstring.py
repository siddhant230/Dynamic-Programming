class Solution: 
    def longestPalindrome(self, s):
    	word=''
    	n=len(s)
    	dp=[[None for i in range(n)] for i in range(n)]
    	k=0
    	for i in range(n):
    		dp[i][i]=True
    	
    	for i in range(1,n):
    		k+=1
    		#printer(dp)
    		for j in range(1,n-k):			
    			start=j
 	   		end=j+k
 	   		
 	   		if s[start]==s[end]:
 	   			if len(s[start:end+1])==2:
 	   				dp[start][end]=True
 	   	
 	   			if dp[start+1][end-1]==True:
 	   				val=len(s[start:end+1])
 	   				dp[start][end]=True
 	   				word=s[start:end+1]
    	return word

def printer(dp):
	for i in dp:
		print(i)
	print('#######')
s = "banana"
#s='million'
s='tracecars'
print(str(Solution().longestPalindrome(s)))