from collections import deque
from typing import List, Optional

from TreeNode import TreeNode


class BinaryTreeExample:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def preorder(root):
            if not root:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return res

    def preorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stk = []
        # stk = deque()
        # stk.append(root)
        # while len(stk) > 0:
        #    root = stk.pop()
        #    if not root:
        #        continue
        #    res.append(root.val)
        #    stk.append(root.right)
        #    stk.append(root.left)
        while root or stk:
            while root:
                res.append(root.val)
                stk.append(root)
                root = root.left
            root = stk.pop()
            root = root.right
        return res

    def preorderTraversal3(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        cur = root
        while cur:
            most_right = cur.left
            if most_right:
                while most_right.right and most_right.right != cur:
                    most_right = most_right.right
                if not most_right.right:
                    most_right.right = cur
                    res.append(cur.val)
                    cur = cur.left
                    continue
                else:
                    most_right.right = None
            else:
                res.append(cur.val)
            cur = cur.right
        return res

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(root: Optional[TreeNode]):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)
        return res

    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stk = []
        while root or stk:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            res.append(root.val)
            root = root.right
        return res

    def inorderTraversal3(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        cur = root
        while cur:
            most_right = cur.left
            if most_right:
                while most_right.right and most_right.right != cur:
                    most_right = most_right.right
                if not most_right.right:  # 建立morris链接
                    most_right.right = cur
                    cur = cur.left
                    continue
                else:  # 删除morris链接
                    most_right.right = None
            res.append(cur.val)
            cur = cur.right
        return res

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def postorder(root):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)

        postorder(root)
        return res

    def postorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stk = []
        while root or stk:
            while root:
                res.append(root.val)
                stk.append(root)
                root = root.right
            tmp = stk.pop()
            root = tmp.left
        res.reverse()
        return res

    def postorderTraversal3(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def reverse(head: Optional[TreeNode]) -> TreeNode:
            prev, next_node, cur_node = None, None, head
            while cur_node:
                next_node = cur_node.right
                cur_node.right = prev
                prev = cur_node
                cur_node = next_node
            return prev

        def process_res(head: Optional[TreeNode]):
            tail = reverse(head)
            while tail:
                res.append(tail.val)
                tail = tail.right
            reverse(tail)

        if not root:
            return res
        cur = root
        while cur:
            most_right = cur.left
            if most_right:
                while most_right.right and most_right.right != cur:
                    most_right = most_right.right
                if not most_right.right:
                    most_right.right = cur
                    cur = cur.left
                    continue
                else:
                    most_right.right = None
                    process_res(cur.left)
            cur = cur.right
        process_res(root)
        return res

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = list()

        def levelOrder1(root: TreeNode, level: int):
            if not root:
                return
            if len(res) <= level:
                res.insert(level, list())
            t = res[level]
            t.append(root.val)
            levelOrder1(root.left, level + 1)
            levelOrder1(root.right, level + 1)

        levelOrder1(root, 0)
        return res

    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        res = list()
        queue = deque()
        queue.append(root)
        level = 0
        while queue:
            size = len(queue)
            for i in range(size):
                tmp = queue.popleft()
                if tmp:
                    if len(res) <= level:
                        res.insert(level, list())
                    ret = res[level]
                    ret.append(tmp.val)
                    queue.append(tmp.left)
                    queue.append(tmp.right)
            level += 1
        return res
