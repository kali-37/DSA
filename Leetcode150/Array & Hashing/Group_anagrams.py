import time

class Solution:
    def groupAnagrams(self,strs:list[str])->list[list[str]]:
        dicter={}
        for i in strs:
            sortedword="".join(sorted(i))
            if sortedword not in dicter:
                dicter[sortedword]=[i]
            else:
                dicter[sortedword].append(i)
        return list(dicter.values())
        
solver=Solution()
print(solver.groupAnagrams(["mango","tango","ognam","gvaua","guava","ganom"]))
