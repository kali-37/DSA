class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        '''
# using nested for loop 

        for i in range(len(nums)):
            for j in range((i+1),len(nums)): 
                if (nums[i]+nums[j]==target):
                    return [i,j]
        return False        
Time complexity of this problem is O(n^2)  
space complexity of this problem is O(1) 

'''
# using hashmap , actually hashmap creates a memory of the value and index of the value
# so that we don't have to travelsal up and down to find the value and index of the value
# so it's time complexity is O(n) and space complexity is O(n)

        hashmap={}
        for i,j in enumerate(nums):
            if  not target-j in hashmap: 
                hashmap[j]=i
            else:
                return [hashmap[target-j],i] 

solver=Solution()
print(solver.twoSum([1,2,3,4,5,6,7,8,9],18))


