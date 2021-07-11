import sys
sys.path.append("..")
from Stack.Stack import Stack

Stack_ = Stack()

def infix2postfix(infix):
    token = list(infix)
    for i in token:
        if not is_operator(i):
            print(i,end="")
        else:
            if i == ")":
                item = Stack_.pop()
                while(item != "("):
                    print(item,end="")
                    item = Stack_.pop()
            else:
               if compare_priority(i) == ">":
                    Stack_.push(i)
               else:
                   item = Stack_.pop()
                   print(item, end="")
                   while (compare_priority(item) != ">"):
                       Stack_.show_stack_form_top()
                       print(item, end="")
                       item = Stack_.pop()
                   Stack_.push(i)
    while(not Stack_.isempty()):
        item = Stack_.pop()
        print(item, end="")

def is_operator(token):
    operator_list = ["(",")","-","^","*","/","+","-",">","<","~","&","|","="]
    if token in operator_list:
        return True
    else:
        return False

def compare_priority(item):
    outside_of_stack = {"(":10,"-":9,"^":8,"*":7,"/":7,"+":6,"-":6,">":5,"<":5,"~":4,"&":3,"|":3,"=":2}
    inside_of_stack = {"(":1,"-":9,"^":8,"*":7,"/":7,"+":6,"-":6,">":5,"<":5,"~":4,"&":3,"|":3,"=":2}
    if not Stack_.isempty():
        if outside_of_stack[item] > inside_of_stack[Stack_.top.data]:
            return ">"
        elif outside_of_stack[item] == inside_of_stack[Stack_.top.data]:
            return "="
        else:
            return "<"
    else:
        return ">"

if __name__ == "__main__":
    infix = "a*(b+c/d)+e"
    infix2postfix(infix)