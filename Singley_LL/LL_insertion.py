class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        point_node = self.head
        while point_node:
            print(point_node.data)
            point_node = point_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prv_node, data):
        if not prv_node:
            print("node not present")
            return
        new_node = Node(data)
        new_node.next = prv_node.next
        prv_node.next = new_node


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.prepend("D")

llist.insert_after_node(llist.head.next, "F")
llist.print_list()
