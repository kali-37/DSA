# https://leetcode.com/problems/container-with-most-water/


class Solution:
    def maxArea(self, height: list[int]) -> int:
        pointerL,pointerR=0,len(height)-1
        res=0
        while(pointerL<pointerR):
            high=height[pointerR]-height[pointerL] 
            print("HIGH",high)
            if(high <0):
                res=max(res,height[pointerR]*(pointerR-pointerL))
                pointerR-=1
            else:
                res=max(res,height[pointerL]*(pointerR-pointerL))
                pointerL+=1
            print("RES",res)
        return res


solver=Solution()
print(solver.maxArea([1,1,4]))