#  https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashtable={} 
        for i in nums:
            if i  in hashtable:
                hashtable[i]+=1
            else:
                hashtable[i]=1
        rearrange=sorted(list(hashtable.values()),reverse=True)[:k]
        returner=[]
        print("rearrange",rearrange[:3])
        for key,value in hashtable.items():
                if value in rearrange:
                    print("value",value, "key",key)
                    returner.append(key)
        return returner

solver=Solution()
print(solver.topKFrequent([1,2,3,4,1,1,2,1,2,11,23,23,234,32,1,12,123,123,12,213,123,123,123,123],3) )
