class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]
        

        for n1Index, n1 in enumerate(nums):
            try:
                n2Index = nums.index(target-n1)
                if n2Index != n1Index:
                    return([n1Index,n2Index])
                continue 
            except:
                continue
def twoSumOptimized(self, nums: List[int], target: int) -> List[int]:
         if len(nums) == 2:
            return [0,1]
         n1Index = 0
         n2Index = len(nums)-1

         numsoriginalOrder = []
         for index, num in enumerate(nums):
            numsoriginalOrder.append([num,index])

         numsSorted = sorted(numsoriginalOrder)
   
         while True:
             calculation = numsSorted[n1Index][0] + numsSorted[n2Index][0]
             if(calculation == target):
                return [numsSorted[n1Index][1], numsSorted[n2Index][1]]
             elif(calculation < target):
                n1Index += 1
             else:
                n2Index -= 1
        
        #3 ms execution time, seems liek too many people use this kind of solution, otherwise, I would have obtained a better response. in my case it was only 51.17 percentil 
    

    