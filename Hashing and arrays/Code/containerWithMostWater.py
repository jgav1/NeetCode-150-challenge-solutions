class Solution(object):
    def maxArea(self, height):

        # brute force is to find a pair that maximixes the output 2 for loops
        # exploratory to be more efficient 2 pointers from the extremes
        # the pointer to be moved is the one that has a smaller value of height

        pi,pf=0,len(height)-1
        maxValue=0

        while (pi < pf):
            maxValue = max(maxValue,min(height[pi],height[pf])*(pf-pi))
            if(height[pi]<=height[pf]):
                pi+=1
            else:
                pf-=1
        return maxValue



        
        #best performance: 108 ms 70 percentil, 20.77 mb 54.73 percentil