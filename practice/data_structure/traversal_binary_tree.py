class Node(object):
    """节点"""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree(object):
    def __init__(self):
        self.root = Node()
        self.queue = []

    def add(self, data):
        """添加节点"""
        node = Node(data)
        if self.root.data == None:  # 如果树为空，则对根节点赋值
            self.root = node
            self.queue.append(self.root)
        else:
            treeNode = self.queue[0]  # 此节点的子树没有齐(当前节点)
            if treeNode.left == None:
                treeNode.left = node
                self.queue.append(treeNode.left)
            else:
                treeNode.right = node
                self.queue.append(treeNode.right)
                self.queue.pop(0)  # 如果该节点存在左右树，将此节点丢弃

    def pre_order_by_recursion(self, root):
        """递归实现先序遍历"""
        if root is None:
            return []
        left_item = self.pre_order_by_recursion(root.left)
        right_item = self.pre_order_by_recursion(root.right)
        return [root.data] + left_item + right_item

    def in_order_by_recursion(self, root):
        """递归实现中序遍历"""
        if root is None:
            return []
        left_item = self.in_order_by_recursion(root.left)
        right_item = self.in_order_by_recursion(root.right)
        return left_item + [root.data] + right_item

    def post_order_by_recursion(self, root):
        """递归实现后序遍历"""
        if root is None:
            return []
        left_item = self.post_order_by_recursion(root.left)
        right_item = self.post_order_by_recursion(root.right)
        return left_item + right_item + [root.data]

    def pre_order_by_stack(self, root):
        """利用堆栈实现先序遍历"""
        if root is None:
            return []
        stack, result = [], []
        node = root
        while node or stack:
            while node:  # 从根节点开始，一直找他的左子树
                result.append(node.data)
                stack.append(node)
                node = node.left
            # while结束表示当前节点node为空，即前一个节点没有左子树了
            node = stack.pop()
            node = node.right  # 开始查看右子树
        return result

    def in_order_by_stack(self, root):
        """利用堆栈实现中序遍历"""
        if root is None:
            return []
        stack, result = [], []
        node = root
        while node or stack:
            while node:  # 从根节点开始，一直找他的左子树
                stack.append(node)
                node = node.left
            # while结束表示当前节点node为空，即前一个节点没有左子树了
            node = stack.pop()
            result.append(node.data)
            node = node.right  # 开始查看右子树
        return result

    def post_order_by_stack(self, root):
        """利用堆栈实现后序遍历"""
        if root is None:
            return []
        stack_1, stack_2, result = [], [], []
        node = root
        stack_1.append(node)
        while stack_1:  # #这个while循环的功能是找出后序遍历的逆序，存在stack_2里面
            node = stack_1.pop()
            if node.left:
                stack_1.append(node.left)
            if node.right:
                stack_1.append(node.right)
            stack_2.append(node)
        while stack_2:  #将stack_2中的元素出栈，即为后序遍历次序
            item = stack_2.pop()
            result.append(item.data)
        return result

    def level_queue(self, root):
        """队列实现树的层次遍历"""
        if root is None:
            return []
        queue, result = [], []
        node = root
        queue.append(node)
        while queue:
            node = queue.pop(0)
            result.append(node.data)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        return result


if __name__ == '__main__':
    tree = Tree()
    for r in range(10):
        tree.add(r)
    print('递归先序遍历：', tree.pre_order_by_recursion(tree.root))  # [0, 1, 3, 7, 8, 4, 9, 2, 5, 6]
    print('堆栈先序遍历：', tree.pre_order_by_stack(tree.root))  # [0, 1, 3, 7, 8, 4, 9, 2, 5, 6]
    print('-' * 50)
    print('递归中序遍历：', tree.in_order_by_recursion(tree.root))  # [7, 3, 8, 1, 9, 4, 0, 5, 2, 6]
    print('堆栈中序遍历：', tree.in_order_by_stack(tree.root))  # [7, 3, 8, 1, 9, 4, 0, 5, 2, 6]
    print('-' * 50)
    print('递归后序遍历：', tree.post_order_by_recursion(tree.root))  # [7, 8, 3, 9, 4, 1, 5, 6, 2, 0]
    print('堆栈后续序遍历：', tree.post_order_by_stack(tree.root))  # [7, 8, 3, 9, 4, 1, 5, 6, 2, 0]
    print('-' * 50)
    print('队列实现树的层次遍历：', tree.level_queue(tree.root))
