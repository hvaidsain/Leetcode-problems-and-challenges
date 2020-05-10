# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Note: Do not use any built-in library function such as sqrt.


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        first = 1
        last = num
        
        while(first <= last):
            
            mid = (first+last)//2            
            res = mid**2
            
            if res == num:
                return True
            elif res>num:
                last = mid-1
            else:
                first = mid+1
                
        return False
        
        