# Given an arbitrary ransom note string and another string containing letters from all the magazines, 
# write a function that will return true if the ransom note can be constructed from the magazines ; 
# otherwise, it will return false.

# Each letter in the magazine string can only be used once in your ransom note.

# Note:
# You may assume that both strings contain only lowercase letters.


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        d = dict()
        
        for c in magazine:
            if c in d:
                d[c] = d[c] + 1
            else:
                d[c] = 1
                
        for c in ransomNote:
            if(c in d and d[c] != 0):
                d[c] = d[c] - 1
            else:
                return False
            
        return True