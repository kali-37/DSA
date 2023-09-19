
# https://leetcode.com/problems/valid-palindrome/


class Solution:
    def isPalindrome(self, ser: str) -> bool:
       # return reversed(s)==s     MUST EASY SOLUTION BUT >> 
        ser=[]
       # let's use two pointers .. and go after it . 
        for se in s:
            if se.isalnum():
                ser.append(se.lower())
        front,rear=0,len(ser)-1
        if (ser==[]):
            return True

        while(ser[front]==ser[rear]):
                if (rear<=front):        
                    return True 
                front+=1
                rear-=1
        return False


solver=Solution()
print(solver.isPalindrome(" "))
