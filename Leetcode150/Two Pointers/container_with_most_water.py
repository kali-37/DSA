# https://leetcode.com/problems/container-with-most-water/


class Solution:
    def maxArea(self, height: list[int]) -> int:
        pointerR=len(height)-1
        res=0
        odd_even_checker=0
        while(pointerR>0):
            pointerL=0
            while(height[pointerL]<height[pointerR]):
                if(height[pointerL]<height[pointerR]):
                    res=max(res,height[pointerL]*height[pointerL])
                else:
                    res=max(res,height[pointerR]*height[pointerR])
                pointerL+=1
            pointerR-=1
        return res


solver=Solution()
print(solver.maxArea([99,10000,1,2]))