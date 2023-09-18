# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res=[1]*len(nums)
        print(res)
        postfix=1   
        prefix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]

        print(res)
        
        for i in range(len(nums) -1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        return res
solver=Solution()
print(solver.productExceptSelf([7,2,3,4]))
