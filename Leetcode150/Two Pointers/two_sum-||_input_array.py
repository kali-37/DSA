
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        result=[]
        for index,value in enumerate(numbers):  # it takes 0(n)
            temp=target-value
            if temp  in numbers:   # it take 0(n) because searching in array takes time of n if it's at last.
                result.append(index+1)
                if  value!=numbers[index+1]:
                    result.append(numbers.index(temp)+1)
                else:
                    result.append(numbers.index(temp)+2)
                return result


#As it's from two pointers , let's solve it using two pointers.

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        result=[]
        l,r=0,len( numbers)-1

        while l<r : 
            if (numbers[l]+numbers[r])==target:
                return [l+1,r+1]
            if(numbers[l]+numbers[r])>target:
                r=r-1
            else:
                l=l+1
        


solver=Solution()
print(solver.twoSum([0,0,1,6,9],0))