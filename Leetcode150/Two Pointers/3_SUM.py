# https://leetcode.com/problems/3sum/


# It is extension of 2 sum , but we have another for all instances . And it can't have duplicates of all..

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sort=sorted(nums)
        print(sort)
        # seter=set(sort)
        res=[]
        for index,value in  enumerate(sort):
            if(index>0)and sort[index-1]==value:
                    continue
            l=index+1
            r=len(sort)-1
            while(l<r):
                if (r==index):
                    r-=1
                if(value+sort[l]+sort[r])==0:
                    res.append([value,sort[l],sort[r]])
                    l+=1 
                    r-=1
                if(value+sort[l]+sort[r])>0:
                    r-=1
                if(value+sort[l]+sort[r])<0:
                    l+=1    
        return res
solver=Solution()
print(solver.threeSum([-1,0,1,2,-1,-4]))