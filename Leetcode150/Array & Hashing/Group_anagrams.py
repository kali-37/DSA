#https://leetcode.com/problems/group-anagrams/

from collections import defaultdict
class Solution:
    # time complexity of this below solution is 0(N*K) where N is the length of strs and K is the maximum length of a string in strs
    def groupAnagrams(self,strs:list[str])->list[list[str]]:
        res=defaultdict(list) 
        for s in strs:
            count=[0]*26
            # print(count)
            for c in s:
                count[ord(c) -ord("a")]+=1
            res[tuple(count)].append(s) # used tuple here because list is not hashable but tuple is hashable



        return list(res.keys()) 

# import time

# class Solution:
# below solution time complexity is O(NKlogK) where N is the length of strs and K is the maximum length of a string in strs``
#     def groupAnagrams(self,strs:list[str])->list[list[str]]:
#         dicter=defaultdict(list)
#         for i in strs:
#             sortedword="".join(sorted(i))  
#             dicter[sortedword].append(i)
#         return list(dicter.values())
            

        
solver=Solution()
print(solver.groupAnagrams(["mango","tango","ognam","gvaua","guava","ganom"]))
