class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max=0

        def height(root):
            if root==None:
                return 0


            left=height(root.left)
            right=height(root.right)

            self.max=max(self.max,left+right)


            return 1+max(left,right)


        height(root)

        return self.max 
