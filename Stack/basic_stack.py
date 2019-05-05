class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def get_stack(self):
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
