# https://skillsmart.ru/algo/py-kf32y/y6a342a5104u.html

class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        nodes = list()
        node = self.head
        while node is not None:
            if node.value == val:
                nodes.append(node)
            node = node.next
        return nodes

    def delete(self, val, all=False):
        node = self.head
        while node is not None:
            if node.value == val:
                if self.head == node and self.tail == node:
                    self.head = None
                    self.tail = None
                elif self.head != node and self.tail != node:
                    node.prev.next, node.next.prev = node.next, node.prev
                elif self.tail == node:
                    self.tail = node.prev
                    node.prev.next = node.next
                elif self.head == node:
                    self.head = node.next
                    node.next.prev = node.prev
                if not all:
                    return
            node = node.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        n = 0
        node = self.head
        while node is not None:
            n += 1
            node = node.next
        return n

    def insert(self, afterNode, newNode):
        if afterNode is None:
            if not self.len():
                newNode.prev = self.head.prev
                newNode.next, self.head.prev = self.head, newNode
                self.head = newNode
            else:
                self.tail.next, newNode.prev = newNode, self.tail
                newNode.next = self.tail.next
                self.tail = newNode
        else:
            if self.head is not None:
                if self.tail == afterNode:
                    self.tail = newNode
                afterNode.next, newNode.next = newNode, afterNode.next

    def add_in_head(self, newNode):
        node = self.head
        if node:
            newNode.next, node.prev = node, newNode
        else:
            newNode.next = None
        self.head = newNode        
