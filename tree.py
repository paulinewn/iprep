BST: Given a node determine if a valid BST ---------------------------------------------------
class Node:
	def __init__ (self, x):
		self.val=x
		self.left= None
		self.right= None

class Solution:
	def isValidBST(self, root):
		return self.isValidBSTRec(root, float("-infinity"), float("infinity"))

		def isValidBSTRec (self, root, min, max):
			if root==None:
				return True
			if root.val <=min or root.val >=max:
				return False
			solution = self.isValidVSTRec(root.left, min, root.val)
			solution = solution and self.isValidVST(root.right, root.val, max)
			return solution

BST: Given a binary search tree and target, find closest number to target----------------------
BT: Top view of binary tree -----------------------------------------------------------

BT: Return deepest node of binary tree  ------------------------------------------------

BT: Inrder traversal ----------
BT: Postorder traversal -------
