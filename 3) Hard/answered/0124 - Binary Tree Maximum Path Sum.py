# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.maxSum = -1 * float("inf")
    
    def maxPathSum(self, root):
        self.postOrderDfs(root)
        return self.maxSum
    
    def postOrderDfs(self,root):
        if root == None:
            return 0
        
        # limit the returned negative values of a leaf node to 0
        left =  max(0,self.postOrderDfs(root.left))
        right = max(0,self.postOrderDfs(root.right))
        
        # update global maximum path to self OR current sub tree
        self.maxSum = max(self.maxSum,(left+right+root.val))
        # return the max between child nodes and father node
        return max(left,right)+root.val

#*-------Tests-------#
sol = Solution()
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
testResult1=sol.maxPathSum(root1)
print(f"Max Path Sum: {testResult1}")  # Expected to compute the maximum path sum for this tree.
#-----------------------------# 
# Construct the binary tree as shown in the image.
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-10)

root.left.left = TreeNode(-5)
root.left.right = TreeNode(1)

root.right.left = TreeNode(50)
root.right.right = TreeNode(20)

# Test case using the constructed tree.
sol = Solution()
testResult2 = sol.maxPathSum(root)
print(f"Max Path Sum: {testResult2}")  # Expected to compute the maximum path sum for this tree.
#*-------------------#
#^ Time Complexity:
#^      O(N)
#^ Space Complexity: 
#^      O(H), where H is height of the tree. 
#^      worst case - O(N) 
#^      best case (balanced tree) - O(log N)