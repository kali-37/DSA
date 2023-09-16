class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        print("i am total num",len(nums))
        for i in range(0,len(nums)-1): # is same as for i in range(len(nums)): because it's start from 0
      # so it will iterate from 0 to len(nums)-1 i.e 0 to 4
            for j in range((i+1),len(nums)): # and this will iterate from 1 to len(nums) i.e 1 to 5
                
                print("comapring",i,j)
                if (nums[i]+nums[j]==target):
                    return True
        return False        



solver=Solution()
print(solver.twoSum([1,2,3,4,5],69))