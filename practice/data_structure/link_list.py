"""
python实现单向链表
"""


class Node(object):
    '''
    data: 节点保存的数据
    _next: 保存下一个节点对象
    '''
    def __init__(self, data, next=None):
        self.data = data
        self._next = next

    def __repr__(self):
        '''
        用来定义Node的字符输出，print为输出的data
        :return:
        '''
        return str(self.data)


# 定义链表类：

# 属性：
# 链表头：head
# 链表长度：length
# 方法：
# 判断链表是否为空：isEmpty()

class LinkList(object):
    def __init__(self):
        self._head = None
        self.length = 0

    def isEmpty(self):
        return (self.length == 0)

    def append(self, dataNode):
        """增加一个节点（在链表尾部追加）"""
        item = None
        if isinstance(dataNode, Node):
            item = dataNode
        else:
            item = Node(dataNode)
        # 链表头为空
        if not self._head:
            self._head = item
            self.length += 1
        else:
            node = self._head
            # 遍历到链表的最后一个节点
            while node._next:
                node = node._next
            node._next = item
            self.length += 1

    def delete(self, index):
        """删除一个节点之后要把链表长度减1"""
        # 如果为空链表
        if self.isEmpty():
            print('链表为空，不支持删除节点操作')
            return

        if index < 0 or index >= self.length:
            print('请输入正确索引值')
            return
        elif index == 0:
            self._head = self._head._next
            self.length -= 1
            return
        else:
            node = self._head
            count = 0
            while True:
                count += 1
                if index == count:
                    node._next = node._next._next
                    break
                node = node._next

        self.length -= 1

    def update(self, index, data):
        """修改一个节点"""
        if self.isEmpty() or index < 0 or index > self.length:
            print('请输入正确索引值')
            return
        j = 0
        node = self._head
        while node._next and j < index:
            node = node._next
            j += 1

        if j == index:
            node.data = data

    def getItem(self, index):
        """查找一个节点"""
        if self.isEmpty() or index < 0 or index > self.length:
            print('请输入正确索引值')
            return
        j = 0
        node = self._head
        while node._next and j < index:
            node = node._next
            j += 1
        return node.data

    def getIndex(self, data):
        """查找一个节点的索引"""
        j = 0
        if self.isEmpty():
            print('链表为空')
            return

        node = self._head
        while node:
            if node.data == data:
                return j
            node = node._next
            j += 1
        if j == self.length:
            print('元素{}没有被找到'.format(data))
            return

    def insert(self, index, dataOrNode):
        if self.isEmpty():
            print('链表为空，不支持insert操作')
            return

        if index < 0 or index >= self.length:
            print('请输入正确索引值')
            return

        item = None
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        if index == 0:
            item._next = self._head
            self._head = item
            self.length += 1
            return

        j = 0
        node = self._head
        prev = self._head
        while node._next and j < index:
            prev = node
            node = node._next
            j += 1

        if j == index:
            item._next = node
            prev._next = item
            self.length += 1

    def clear(self):
        """清空链表"""
        self._head = Node
        self.length = 0

    def __repr__(self):
        if self.isEmpty():
            print('链表为空')

        li = ""
        node = self._head
        while node:
            li += str(node.data) + ' '
            node = node._next
        return li

