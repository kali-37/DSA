# link: https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self,nums:list[int])->bool:
        hashset=set()
        for n in nums: 
            if n in hashset :
                return True
            hashset.add(n)
        return False


# Path: Leetcode150/Array & Hashing/Contains_Duplicate.py
Solution=Solution()
print(Solution.containsDuplicate([1,2,3,1]))