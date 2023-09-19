# link : https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        res=[]
        if(nums==[]):
            return 0
        count_str=[1]
        while( len(nums)>1):
            delemiter=1
            s=max(nums)
            nums.remove(s)
            while(s-max(nums))==1:
                delemiter+=1
                count_str.append(delemiter)
                if len(nums)>1:
                    s=max(nums)
                    nums.remove(s)
                else:
                    break
        return max(count_str)



solver=Solution()
print(solver.longestConsecutive([]))
        