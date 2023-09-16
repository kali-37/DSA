#link : https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self,s:str,t:str)->bool:

      #   return sorted(s)==sorted(t)  # Solution 1  is perfect solution for this 
      #   return counter(s)==counter(t)  # Solution 2  is same as Hashmap but more efficent because it's builtin hashmap like 

       # Using Hashmap regural using dict,  
        if len(s)!=len(t):  
            return False 
        dictS,dictT={},{} 
        for i in range(len(s)):
            dictS[s[i]]=1+dictS.get(s[i],0)  # gives value of s[i] , if not exits then provide 0 
            dictT[s[i]]=1+dictT.get(s[i],0)
        return dictT==dictS


Solver=Solution()
print(Solver.isAnagram("anagram","nagrama"))