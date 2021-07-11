import sys
sys.path.append("..")
from Node.Node import ListNode

class Stack():
    def __init__(self):
        self.top = None

    def push(self, item):
        t = ListNode(item)
        t.next = self.top
        self.top = t

    def pop(self):
        if self.isempty():
            print("Can not pop. Stack is empty.")
        else:
            item = self.top.data
            self.top = self.top.next
            return item

    def isempty(self):
        return(self.top == None)

    def show_stack_form_top(self):
        print("Stack :",end=" ")
        pointer = self.top
        while(pointer != None):
            print(pointer.data, end=" ")
            pointer = pointer.next
        print("")

if __name__ == "__main__":
    Stack_ = Stack()
    Stack_.push(3)
    Stack_.show_stack_form_top()
    Stack_.push(2)
    Stack_.show_stack_form_top()
    Stack_.push(1)
    Stack_.show_stack_form_top()
    Stack_.pop()
    Stack_.show_stack_form_top()
