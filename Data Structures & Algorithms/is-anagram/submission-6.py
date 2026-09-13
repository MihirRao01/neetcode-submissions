class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        my_dict_s = {}
        for char in s :
            my_dict_s[char] = my_dict_s.get(char,0) + 1

        my_dict_t = {}
        for char in t:
            my_dict_t[char] = my_dict_t.get(char,0) + 1
        
        for key,value in my_dict_s.items():
            if my_dict_t.get(key) != value:
                return False
    
        return True
        