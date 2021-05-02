
# A LinkedList node
class Node:

    # Constructor to create a new node
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node:
            nodes.append(node.data)
            node = node.next
        return str(nodes)

    def __iter__(self):
        node = self.head
        while node:
            '''
            带yield的函数是一个生成器，而不是一个函数了，这个生成器有一个
            函数就是next函数，next就相当于“下一步”生成哪个数，这一次的next开始的地方是接着上一次的next停止的地方执行的，所以调用next的时候，生成器并不会从foo函数的开始执行，只是接着上一步停止的地方开始，然后遇到yield后，return出要生成的数，此步就结束。
            '''
            yield node
            node = node.next

    def add_first(self,node):
        node.next = self.head
        self.head = node

    def add_tail(self,node):
        if not self.head:
            self.head = node
            return
        for curr_node in self:
            pass
        curr_node.next = node

    # insert after an existing node
    def insert_after(self,targetNodeData,new_node):
        if not self.head:
            raise Exception("list is empty")
        # traverse the LL
        for node in self:
            if node.data == targetNodeData:
                new_node.next = node.next
                node.next = new_node
                break


    def insert_before(self,targetNodeData,new_node):
        if not self.head:
            raise Exception("list is empty")

        if self.head.data == targetNodeData:
            self.add_first(new_node)

        curr = self.head
        while curr.next:
            if curr.next.data == targetNodeData:
                new_node.next = curr.next
                curr.next = new_node
                return
            curr = curr.next

        # if node doesn't exist
        raise Exception("Node '%s' nof found" %targetNodeData)

    def remove_node(self,targetNodeData):
        if not self.head:
            raise Exception("list is empty")
        if self.head.data == targetNodeData:
            self.head = self.head.next
            return

        curr = self.head
        while curr.next:
            if curr.next.data == targetNodeData:
                curr.next = curr.next.next
                return
            curr = curr.next
        raise Exception("Node '%s' nof found" % targetNodeData)








