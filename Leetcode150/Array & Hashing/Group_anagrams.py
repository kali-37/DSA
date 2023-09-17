import time
from collections import defaultdict
class Solution:
    def groupAnagrams(self,strs:list[str])->list[list[str]]:
        res=defaultdict(list) 
        for s in strs:
            count=[0]*26
            # print(count)
            for c in s:
                count[ord(c) -ord("a")]+=1
            res[tuple(count)].append(s)
        return list(res.values())


# import time
# from collections import defaultdict
# class Solution:
#     def groupAnagrams(self,strs:list[str])->list[list[str]]:
#         res=defaultdict(list) 
#         for s in strs:
#             count=[0]*26
#             # print(count)
#             for c in s:
#                 count[ord(c) -ord("a")]+=1
#             res[tuple(count)].append(s)
#         return list(res.values())
            

        
solver=Solution()
print(solver.groupAnagrams(["mango","tango","ognam","gvaua","guava","ganom"]))
