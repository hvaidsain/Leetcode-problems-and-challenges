# Given a positive integer, output its complement number. 
# The complement strategy is to flip the bits of its binary representation.

class Solution:
    def findComplement(self, n: int) -> int:
        
        def decToBinary(n):
            binary = ""
            while(n>0):
                
                mod = n % 2
                binary = str(mod) + binary
                n = n//2
                
            return binary
        
        def complement(s):
            q = ""
            
            for c in s:
                if c == "0":
                    q = q+"1"
                else:
                    q = q+"0"
                    
            return q
        
        def binToDecimal(s):
            
            i = 0
            j = len(s)-1
            decimal = 0
            while(j>=0):
                decimal  = decimal + int(s[j])*pow(2,i)
                
                i+=1
                j-=1
                
            return decimal
            
                
        s = decToBinary(n)
        
        s = complement(s)
        
        ans = binToDecimal(s)
        
        
        return ans
        
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                
                
        