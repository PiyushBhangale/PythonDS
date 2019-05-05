"""
Stack Datastructure
"""


class Stack:
    def __init__(self):  # Constructor that defines the list of stack
        self.items = []

    def is_empty(self):  # To check if stack is empty
        return self.items == []

    def peek(self):  # Return the topmost element
        if not self.is_empty():
            return self.items[-1]

    def push(self, item):  # push element to top of stack
        self.items.append(item)

    def pop(self):  # pop element at top of stack
        return self.items.pop()

    def get_stack(self):  # get the entire stack
        return self.items


s1 = Stack()
print(s1.is_empty())
s1.push("A")
s1.push("B")
print(s1.get_stack())
s1.push("C")
print(s1.peek())
print(s1.is_empty())
print(s1.get_stack())
s1.pop()
print(s1.get_stack())
