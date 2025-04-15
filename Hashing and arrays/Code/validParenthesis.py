class Solution(object):
    def isValid(self, s):
        if(len(s)%2):
            return False
        stack=[]
        for c in s:
            if(c=='(' or c=='[' or c=='{'):
                stack.append(c)
            else:
                if(len(stack)==0):
                    return False
                cpop=stack.pop()
                if(cpop =='(' and c!=')' or cpop =='{' and c!='}' or cpop =='[' and c!=']'):
                    return False               
            
        if(len(stack)!=0):
            return False
        return True
                 

        
        #best performance: 1 ms 68.3 percentil, 12.38 mb 99.07 percentil