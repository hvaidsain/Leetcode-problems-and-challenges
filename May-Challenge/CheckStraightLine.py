
# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. 
# Check if these points make a straight line in the XY plane.

class Solution:
    def checkStraightLine(self, a: List[List[int]]) -> bool:
        
        if (a[1][0] - a[0][0]) == 0:
            for i in range(1,len(a)):
                mt = (a[i][0] - a[i-1][0])
            
                if(mt != 0):
                    return False
        
        m = (a[1][1] - a[0][1]) / (a[1][0] - a[0][0])
        
        if (a[1][0] - a[0][0]) != 0:
            
            for i in range(1,len(a)):
                
                den = (a[i][0] - a[i-1][0])
                if(den == 0):
                    return False
            
                mt = (a[i][1] - a[i-1][1]) / (a[i][0] - a[i-1][0])
            
                if(m != mt):
                    return False
        
        
            
        return True
        
        
        
        