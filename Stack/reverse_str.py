from basic_stack import Stack


def reverse_str(stack, inp_str):
    for i in range(len(inp_str)):
        stack.push(inp_str[i])
    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()
    return rev_str


s1 = Stack()
print(reverse_str(s1, "Hello"))
