class SolutionGoodRamBadExecutionTime:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
    
        for currentNum, nextNum in zip(nums, nums[1:]):
            if currentNum == nextNum:
                return True
        
        return False
    
# runtime 52 ms, beats only 5.2% of submissions, memory 27.84 MB, beats 91.08% of submissions
    
class SolutionAttempedOptimization:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return  not (len(set(nums)) == len(nums))
# runtime 9 ms, beats only 62.76% of submissions, memory 31.58 MB, beats 50.34% of submissions

class SolutionBetsSoFar:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        
        for num in nums:
            if num in seen:  
                return True
            seen.add(num)  
        
        return False
# runtime 4 ms, beats only 53.59% of submissions, memory 31.58 MB, beats 50% of submissions


        
        
        
