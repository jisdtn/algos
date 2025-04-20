from typing import Optional

from utils_TreeNode import TreeNode, list_to_binary_tree


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == '__main__':
    tree = list_to_binary_tree([3, 9, 20, None, None, 15, 7])
    print(Solution().maxDepth(tree))
