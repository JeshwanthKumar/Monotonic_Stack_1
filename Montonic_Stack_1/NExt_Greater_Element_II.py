#Time_Complexity: O(n)
#Space_Complexity: O(n)

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        mStack = [] #Initialize a stack as mStack
        result = [-1] * len(nums)   #Initialize result as 1s for the length of nums

        for i in range(2*len(nums)):    #Continue till the 2* length of nums
            while mStack and nums[mStack[-1]] < nums[i%len(nums)]:  #Continu till mStack is True and nums[mStack[-1]] < nums[i%len(nums)]
                result[mStack[-1]] = nums[i%len(nums)]  #Change the result[mStack[-1]] as num[i%len(nums)]
                mStack.pop()    #Pop the last element in mStack
                
                
            if i < len(nums):   #If the index is less than length of nums
                mStack.append(i)    #Append the index into mStack
                
                
        return result   #Return result
                    
                    