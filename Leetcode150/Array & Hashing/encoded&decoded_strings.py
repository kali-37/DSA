
##     <<<< SUBSCRIBE SUBSCRIBE MOTHER F***E* .

# link >   https://leetcode.com/problems/encode-and-decode-strings/


## Wait .. we have https://www.lintcode.com/problem/659/ for free solve link... 

#Design an algorithm to encode a list of strings to a string . The encoded string is then sent over the network and decoded back to original list of strings  . 

# Please Implement encoded and decode 

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):  # here self is 
        # write your code here
        encoders=""
        for s in strs: 
            temp=str(len(s))
            encoders+=f"{temp}#"+s
        return encoders            
        """
    @param: str: A string 
    @return: decodes a single string to a list of strings
    """

    def decode(self, strs):
        i=0
        res=[]
        while(i<len(strs)):
            length=i
            while(i<len(strs) and strs[i]!="#"):
                length=int(strs[i])
                i+=1
            res.append(strs[i+1:length+i+1])
            i+=(1+length)
        return res

    def __str__(self):
        return str(self.strs)


solver=Solution()
print(solver.decode(solver.encode(["we", "say", ":", "yes"])))
