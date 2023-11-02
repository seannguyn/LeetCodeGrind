# https://leetcode.com/problems/closest-binary-search-tree-value/?envType=study-plan-v2&envId=premium-algo-100

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest_value = root.val
        closest_value = self.findClosestValue(closest_value, root, target)
        return closest_value

    def findClosestValue(self, closest_value, root: Optional[TreeNode], target: float):
        if root == None:
            return closest_value

        if abs(root.val - target) < abs(closest_value - target):
            closest_value = root.val
        
        if target > root.val:
            closest_value = self.findClosestValue(closest_value, root.right, target)
        else:
            closest_value = self.findClosestValue(closest_value, root.left, target)
        
        return closest_value

if __name__ == "__main__":
    solution = Solution()