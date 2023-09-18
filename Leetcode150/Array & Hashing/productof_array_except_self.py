# https://leetcode.com/problems/product-of-array-except-self/


# SOlution 1 : 
# class Solution:
#     def productExceptSelf(self, nums: list[int]) -> list[int]:
#         prefix,postfix=[],[]
#         multiplier=1
#         for i in nums:
#             multiplier*=i
#             prefix.append(multiplier)
#         multiplier=1
#         for i in range(len(nums)-1,0,-1):
#             multiplier*=nums[i]
#             postfix.insert(0,multiplier)
#         returner=[]
#         for i in range(1,len(nums)-1):
#             returner.append(prefix[i-1]*postfix[i])            
#         returner.insert(0,postfix[0])
#         returner.append(prefix[len(nums)-2])
#         return returner 


# SOlution 2: is compact version of Solution without having to have extra memory space of 
# 0(n) for both prefix and postfix array

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
