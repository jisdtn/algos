from typing import List, Optional

from utils_TreeNode import list_to_binary_tree, TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            result.append(node.val)
            dfs(node.right)

        dfs(root)
        return result


if __name__ == '__main__':
    root = list_to_binary_tree([1,2,3,4,5,None,8,None,None,6,7,9])
    print(Solution().inorderTraversal(root))
