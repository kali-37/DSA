# import time

# class Solution:
#     def groupAnagrams(self,strs:list[str])->list[list[str]]:
#         dicter=[]
#         sorted_array=[]
#         for s in strs:
#             sorted_array.append("".join(sorted(s)))

#         for i,s in enumerate(sorted_array):
#             si=0
#             for ie,c in enumerate(dicter):
#                 print("c :",c[0])
#                 if sorted_array[c[0]]==s:
#                     si=1
#                     dicter[ie].append(i)
#             if (si==0):
#                 dicter.append([i])
#         return dicter

import time
class Solution:
    def groupAnagrams(self,strs:list[str])->list[list[str]]:
        dicter={}
        sorted_array=[]
        for s in strs:
            sorted_array.append("".join(sorted(s)))

        for i,s in enumerate(sorted_array):
            si=0
            # for ie,c in enumerate(dicter):
            if  
                print("c :",c[0])
                if sorted_array[c[0]]==s:
                    si=1
                    dicter[ie].append(i)
            if (si==0):
                dicter[i]=[s]

        return dicter


solver=Solution()
print(solver.groupAnagrams(["mango","tango","ognam","gvaua","guava","ganom"]))
