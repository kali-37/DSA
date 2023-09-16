class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        '''
# using nested for loop 

        for i in range(len(nums)):
            for j in range((i+1),len(nums)): 
                if (nums[i]+nums[j]==target):
                    return True
        return False        
Time complexity of this problem is O(n^2)  
space complexity of this problem is O(1) 

'''

# Path: Leetcode150/Array & Hashing/Twosum.py
# using sorting and comparing the addition of adjacents values 

        nums=sorted(nums)
        for i in range(len(nums)-1):
            if(nums[i]+nums[i+1])==target:
                return True

        return False
# it's time complexity is O(nlogn) and space complexity is O(1)

solver=Solution()
print(solver.twoSum([1,2,3,4,5,6,7,8,9],10))


