# https://leetcode.com/problems/trapping-rain-water/


class Solution:
    def trap(self, height: list[int]) -> int:
        LTHULO,RTHULO=0,0
        middleObstacles=0
        area=0
        value2=0
        for i in range(0,len(height),2): 
            value1=height[i]
            if (i==len(height)-1):
                if (LTHULO <=value1):
                    area+=value2-LTHULO-middleObstacles
                    continue
            else:
                value2=height[i+1] 
            temp=value1-value2
            if temp >0:
                LTHULO=max(value1,LTHULO)
                middleObstacles=value2+value1
            elif(value2>LTHULO):
                area+=value2-(LTHULO-middleObstacles)
                LTHULO=value2
                middleObstacles=0
        return area


solver=Solution()
print(solver.trap([0,1,0,2,1,0,1,3,2,1,2,1]))



