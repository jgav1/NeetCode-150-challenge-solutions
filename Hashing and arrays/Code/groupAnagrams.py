class Solution:
    def calculateDic(self, strs: List[str]) -> dict:
        toReturn = {}
        for i,str in enumerate(strs):
            alphabet_dict = {
                'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0,
                'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0,
                's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
                }
            for char in str:
                alphabet_dict[char] += 1
           
            for key in list(alphabet_dict.keys()):
                if alphabet_dict[key]==0:
                    del alphabet_dict[key]
            dic = alphabet_dict
            hashable_key = tuple(sorted(dic.items()))
            #print(dic)
            if hashable_key in toReturn:
                toReturn[hashable_key].append(i)
            else:
                toReturn[hashable_key] = [i]
        return toReturn
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == [""]:
            return [[""]]
        if len(strs) == 1:
            return [strs]
        #self.calculateDic(strs)
        print(self.calculateDic(strs))
        dictionaryWithCounters =  self.calculateDic(strs)

        toReturn = [[] for _ in range(len(dictionaryWithCounters))]

        for i, values in enumerate(dictionaryWithCounters.values()):
            #print(i, values)
            result = [strs[j] for j in values]
            #print(result)
            toReturn[i] = result

        return toReturn


        #dictionarized = self.calculateDic(strs)
        #while(dictionarized):
        #    for

# 154 ms beats 5.32% of submissions, 26.94 mb ram beats 9.38% of submissions