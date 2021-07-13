import sys
sys.path.append("..")
from Node.Node import ListNode

class Queue:
    def __init__(self):
        self.Front = None
        self.Rear = None

    def isempty(self):
        if self.Front == None:
            return True
        else:
            return False

    def Enqueue(self,item):
        Node = ListNode(item)
        if (self.Front == None):
            self.Front = Node
        else:
            self.Rear.next = Node
        self.Rear = Node

    def Dequeue(self):
        if self.isempty():
            return  "Queue is empty."
        t = self.Front
        item = t.data
        self.Front = self.Front.next
        if self.Front == None:
            self.Rear = None
        del(t)
        return item

    def show_queue_form_front(self):
        current = self.Front
        print("Queue: ",end="")
        while(current != None):
            print(current.data,end=" ")
            current = current.next
        print()

if __name__ == "__main__":
    Queue_ = Queue()
    Queue_.Enqueue(3)
    Queue_.show_queue_form_front()
    Queue_.Enqueue(4)
    Queue_.show_queue_form_front()
    Queue_.Dequeue()
    Queue_.show_queue_form_front()
    Queue_.Enqueue(1)
    Queue_.show_queue_form_front()
    Queue_.Dequeue()
    Queue_.show_queue_form_front()
    Queue_.Enqueue(5)
    Queue_.show_queue_form_front()
    Queue_.Dequeue()
    Queue_.show_queue_form_front()
    Queue_.Dequeue()
    Queue_.show_queue_form_front()
