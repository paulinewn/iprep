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

BT: Height ----------------------------------------------------
   int height(Node root)
    {
     if (root == null)
         return 0;
     else
        return 1+ Math.max (height (root.left), height (root.right));          
    }

BT: Top view of binary tree -----------------------------------------------------------
void top_view(Node root)
    {
     if (root == null)
         System.out.print("null");
    traverse_left(root.left);
    System.out.print(root.data+" ");
    traverse_right(root.right);
}
public void traverse_left (Node x)
        {
        if (x==null)
            return;
        traverse_left(x.left);
        System.out.print(x.data+" ");
    }
public void traverse_right (Node x)
    {
    if (x==null)
        return;
    System.out.print(x.data + " ");
        traverse_right(x.right);
}

BT: Return deepest node of binary tree  ------------------------------------------------


BT: Inorder traversal ----------

BT: Postorder traversal -------
