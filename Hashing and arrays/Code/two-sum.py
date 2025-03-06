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
        
    