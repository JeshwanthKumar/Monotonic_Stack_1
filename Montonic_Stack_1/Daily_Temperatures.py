#Time_Complexity: O(n)
#Space_Complexity: O(n) - Space required for monotonic stack

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mStack = [] #Initialize a stack as mStack
        result = [0] * len(temperatures)    #Initialize result as 0s for the length of temperatures
        
        for i in range(len(temperatures)):  #Continue till the length of temperatures
            while mStack and temperatures[mStack[-1]] < temperatures[i]:    #Continue till mStack and temperatures[mStack[-1]] < temperatures[i]
                nextWarmer = i - mStack[-1] #Initialize nextWarmer as difference between that index and mStack[-1]
                result[mStack[-1]] = nextWarmer #Change result[mStack[-1]] as nexWarmer
                mStack.pop()    #Pop the last element in the mStack
                
                
            mStack.append(i)    #Append that index into the mStack

        return result   #Return result