# link : https://leetcode.com/problems/longest-consecutive-sequence/

# My solution thought it's long it causes runtime error for large numbers.
# mine one .. 
# class Solution:
#     def longestConsecutive(self, nums: list[int]) -> int:
#         nums=set(nums)
#         if(nums is empty):
#             return 0
#         count_str=[1]
#         while( len(nums)>1):
#             delemiter=1
#             s=max(nums)
#             nums.remove(s)
#             while(s-max(nums))==1:
#                 delemiter+=1
#                 count_str.append(delemiter)
#                 if len(nums)>1:
#                     s=max(nums)
#                     nums.remove(s)
#                 else:
#                     break
#         return max(count_str)



solver=Solution()
print(solver.longestConsecutive([]))
        