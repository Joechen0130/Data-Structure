import sys
sys.path.append("..")
from Stack.Stack import Stack
from infix2postfix import *
Stack_ = Stack()

def Post_Calculate(postfix):
    token = list(postfix)
    for i in token:
        if not is_operator(i):
            Stack_.push(i)
        else:
            op2 = Stack_.pop()
            op1 = Stack_.pop()
            result = Calculate(op1, i, op2)
            Stack_.push(result)
    final_result = Stack_.pop()
    print(final_result)

def Calculate(op1, i, op2):
    if i == "+":
        return int(op1) + int(op2)
    elif i == "-":
        return int(op1) - int(op2)
    elif i == "*":
        return int(op1) * int(op2)
    elif i == "/":
        return float(op1) / float(op2)
    elif i == "^":
        return int(op1) ** int(op2)

if __name__ == "__main__":
    infix = input("Input infix (operand must be number):")
    postfix = infix2postfix(infix)
    Post_Calculate(postfix)