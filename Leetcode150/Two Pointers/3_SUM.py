# https://leetcode.com/problems/3sum/


# It is extension of 2 sum , but we have another for all instances . And it can't have duplicates of all..

# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         sort=sorted(nums)
#         print(sort)
#         # seter=set(sort)
#         res=[]
#         for index,value in  enumerate(sort):
#             if(index>0)and sort[index-1]==value:
#                     continue
#             l=index+1
#             r=len(sort)-1
#             print("INDEX ",index)
#             while(l<r):
#                 while (sort[l]==sort[l-1] and l<r):
#                    l+=1 
#                 if(value+sort[l]+sort[r])==0:
#                     res.append([value,sort[l],sort[r]])
#                     print("yes..")
#                     l+=1 
#                     r-=1
#                 if(value+sort[l]+sort[r])>0:
#                     r-=1
#                 if(value+sort[l]+sort[r])<0:
#                     l+=1    
#         return res



# NEETCODE.IO solution 


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # Skip positive integers
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res





solver=Solution()
print(solver.threeSum([-4, -1, -1, 0, 1, 2]

))