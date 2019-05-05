"""
Balance Parenthesis 
"""

from basic_stack import Stack


def is_match(st1, st2):
    if st1 == '(' and st2 == ')':
        return True
    elif st1 == '{' and st2 == '}':
        return True
    elif st1 == '[' and st2 == ']':
        return True
    else:
        return False


def is_parent_balanced(paren_str):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_str) and is_balanced:
        paren = paren_str[index]
        if paren in "({[":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index += 1
    if s.is_empty() and is_balanced:
        return True
    else:
        return False


print(is_parent_balanced("(({[]}))"))
print(is_parent_balanced("(({[))"))
