class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False  # Exit early if lengths don't match
        
        # Define the alphabet_dict outside the if block
        alphabet_dict_s = {
            'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0,
            'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0,
            's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
        }

        alphabet_dict_t = {
            'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0,
            'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0,
            's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
        }
 # generate the dictionaries that count repetitions of characters       
        for char in s:
            alphabet_dict_s[char] += 1
        for char in t:
            alphabet_dict_t[char] += 1

# improve RAM usage free ram...
        for key in list(alphabet_dict_s.keys()):
            if alphabet_dict_s[key]==0:
                del alphabet_dict_s[key]
        for key in list(alphabet_dict_t.keys()):
            if alphabet_dict_t[key]==0:
                del alphabet_dict_t[key]


        
        return alphabet_dict_s == alphabet_dict_t



# 11 ms beats 74.5% of submissions, or 6 ms depends on the execution in that case beats 92% and 17.78 mb ram beats 59.45% of submissions
