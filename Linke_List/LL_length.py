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

    def delete_node(self, key):
        current_node = self.head

        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return
        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next
        if current_node == None:
            return
        prev_node.next = current_node.next
        current_node = None

    def del_node_at_pos(self, pos):
        curr_node = self.head
        counter = 0
        if pos == 0:
            self.head = curr_node.next
            curr_node = None
            return
        prv_node = None
        while curr_node and pos != counter:
            prv_node = curr_node
            curr_node = curr_node.next
            counter += 1
        if curr_node is None:
            return
        prv_node.next = curr_node.next
        curr_node = None

    def len_iterative(self):
        curr_node = self.head
        counter = 0
        while curr_node:
            counter += 1
            curr_node = curr_node.next
        return counter

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.prepend("D")
llist.append("E")
llist.append("G")

llist.insert_after_node(llist.head.next, "F")
llist.delete_node("F")
llist.delete_node("D")

llist.del_node_at_pos(1)
llist.print_list()
print(llist.len_iterative())
print(llist.len_recursive(llist.head))
