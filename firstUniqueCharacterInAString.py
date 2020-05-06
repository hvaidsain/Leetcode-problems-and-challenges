# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.


class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        d = dict()
        res = -1
        
        for c in s:
            if c in d:
                d[c] = d[c] + 1
            else:
                d[c] = 1
                
        for i in range(0,len(s)):
            if d[s[i]] == 1:
                res = i
                break
                
        return res
            
        