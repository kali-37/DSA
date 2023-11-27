

class Solution:
    def missingNumber(self,array,n):
        # code here
        sums=n*(n+1)//2  # Using math formulae.
        array_sum=sum(array) 
        return sums-array_sum




#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().missingNumber(a,n)
    print(s)