from basic_stack import Stack


def div_by_2(decimal):
    s = Stack()
    while decimal > 0:
        remainder = decimal % 2
        s.push(remainder)
        decimal = decimal//2
    bina = ""

    while not s.is_empty():
        bina += str(s.pop())

    return bina


print(div_by_2(242))
