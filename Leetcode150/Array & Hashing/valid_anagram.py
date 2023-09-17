#link : https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self,s:str,t:str)->bool:

      #   return sorted(s)==sorted(t)  # Solution 1 uses time complexity of O(nlogn) because of sorting
      #   return counter(s)==counter(t)  # Solution 2  uses time complexity of O(n) and space complexity of O(n)

       # Using Hashmap regular using dict,  is same to counter above but uses more lines to right.
        if len(s)!=len(t):  
            return False 
        dictS,dictT={},{} 
        for i in range(len(s)):
            dictS[s[i]]=1+dictS.get(s[i],0)  # gives value of s[i] , if not exits then provide 0 
            dictT[s[i]]=1+dictT.get(s[i],0)
        return dictT==dictS


Solver=Solution()
print(Solver.isAnagram("anagram","nagrama"))