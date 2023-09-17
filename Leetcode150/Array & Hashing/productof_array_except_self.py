# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix=[]
        multiplier=1
        postfix=[]
        for i in nums:
            multiplier*=i
            prefix.append(multiplier)
        print(prefix,"prefix")
        multiplier=1
        for i in range(len(nums)-1,0,-1):
            print("i am num 0 ",nums[0])
            multiplier*=nums[i]

            postfix.insert(0,multiplier)

            # postfix.insert(0,multiplier*num[0])
        print(postfix,"postfix")
        returner=[]
        for i in range(1,len(nums)-1):
            returner.append(prefix[i-1]*postfix[i])            
        returner.insert(0,postfix[0])
        returner.append(prefix[len(nums)-2])
        return returner 

solver=Solution()
print(solver.productExceptSelf([1,2,3,4]))
