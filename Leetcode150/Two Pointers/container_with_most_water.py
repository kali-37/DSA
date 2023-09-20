# https://leetcode.com/problems/container-with-most-water/


class Solution:
    def maxArea(self, height: list[int]) -> int:
        print(height,len(height))
        pointerR=len(height)-1
        res=0
        odd_even_checker=0
        while(pointerR>0):
            pointerL=0
            while(pointerL<pointerR):
                if(pointerL<pointerR):
                    res=max(res,pointerL*pointerL)
                else:
                    res=max(res,pointerR*pointerR)
                pointerL+=1
            pointerR-=1
        return res


solver=Solution()
print(solver.maxArea([1,8,6,2,5,4,8,3,7]))