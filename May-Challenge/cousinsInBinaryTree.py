# In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

# Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

# We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

# Return true if and only if the nodes corresponding to the values x and y are cousins.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        
        def cousinsX(root,value,dep,Xprev):
            
            if(root == None):
                return  None
            
            if(root.val == value):
                return [dep,Xprev]
            
            Xprev = root
            dep = dep + 1
            return cousinsX(root.left,value,dep,Xprev) or cousinsX(root.right,value,dep,Xprev)
        
        def cousinsY(root,value,dep,Yprev):
            
            if(root == None):
                return  None
            
            if(root.val == value):
                return [dep,Yprev]
            
            Yprev = root
            dep = dep + 1
            return cousinsY(root.left,value,dep,Yprev) or cousinsY(root.right,value,dep,Yprev)
        
        depx,prevX = cousinsX(root,x,0,None)
        depy,prevY = cousinsY(root,y,0,None)
        
        if(prevX == prevY):
            return False
        elif(prevX != prevY):
            if(depx == depy):
                return True
            else:
                return False
            
                
                
                
                
                    
                    
            
            
        

 

