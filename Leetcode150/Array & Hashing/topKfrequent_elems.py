#  https://leetcode.com/problems/top-k-frequent-elements/

# class Solution:
#     def topKFrequent(self, nums: list[int], k: int) -> list[int]:
#         hashtable={} 
#         for i in nums:
#             if i  in hashtable:
#                 hashtable[i]+=1
#             else:
#                 hashtable[i]=1
#         rearrange=sorted(list(hashtable.values()),reverse=True)[:k]
#         returner=[]
#         print("rearrange",rearrange[:3])
#         for key,value in hashtable.items():
#                 if value in rearrange:
#                     print("value",value, "key",key)
#                     returner.append(key)
#         return returner

# As , this take nlog(n) times , so let's do it within 0(n) times using bucket sorting. 



class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dicter={}
        lister=[[] for i in range(len(nums)+1)] 
        for i in nums:
            dicter[i]=1+dicter.get(i,0)
        
        for key,value in dicter.items():
            lister[value].append(key)
        answer=[]
        for i in range(len(lister)-1,0,-1):
            for j in lister[i]:
                print(j)
                answer.append(j)
                if (k==len(answer)):
                    return answer 


solver=Solution()
print(solver.topKFrequent([1,1,1,2,2,3],2) )
