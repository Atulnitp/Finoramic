# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers
    def pathSum(self, A, B):
        ls = []
        left = []
        right = []
        if A.left == None and A.right == None and B - A.val == 0:
            temp = []
            temp.append(A.val)
            ls.append(temp)
            return ls
        if A.left != None:
            l = self.pathSum(A.left, B - A.val)
            if len(l) != 0:
                for i, v in enumerate(l):
                    l[i].insert(0, A.val)
                left = l
        if A.right != None:
            r = self.pathSum(A.right, B - A.val)
            if len(r) != 0:
                for i, v in enumerate(r):
                    r[i].insert(0, A.val)
                right = r

        return left + right
