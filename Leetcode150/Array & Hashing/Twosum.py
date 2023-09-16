class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        print("i am total num",len(nums))
        for i in range(len(nums)):
            for j in range((i+1),len(nums)): 
                if (nums[i]+nums[j]==target):
                    return True
        return False        
#Time complexity of this problem is O(n^2)  
# space complexity of this problem is O(1) 



solver=Solution()
print(solver.twoSum([1,2,3,4,5],69))


