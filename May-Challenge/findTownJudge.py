# In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

# If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        if N==1  and len(trust)>=1:
            return -1
        
        
        n = len(trust)
        
        d = dict()
        potential = -1
        
        for i in range(n):
            d[trust[i][0]] = trust[i][1]
            
        for i in range(1,N+1):
            if i not in d:
                potential = i
                break
                
        arr = [0] * (N+1)
        
        if potential == -1:
            return -1
        else:
            for i in range(n):
                arr[trust[i][1]] +=1
                
        if arr[potential] == N-1:
            return potential
        else:
            return -1
            
        
            
            
            
        