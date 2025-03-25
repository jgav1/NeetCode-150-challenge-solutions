#https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dictNums= {}
        dictNums[nums[0]] = 0
        toReturn = []
        #frequency
        for num in nums:
            if(not dictNums.get(num)):
                dictNums[num] = 1
            else:
                dictNums[num] = dictNums[num] + 1
        #sorting
        for ke in sorted(dictNums, key=dictNums.get, reverse=True):
            toReturn.append(ke)        
        return toReturn[0:k]        

# 3 ms beats 91.01% of submissions,  20.96 mb ram beats 96.46% of submissions