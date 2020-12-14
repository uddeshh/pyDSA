class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node
    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def printit(self):
        cur_node=self.head
        while cur_node:
            print(cur_node.data)
            cur_node=cur_node.next
    def insertit(self,prev_node,data):
        if not prev_node:
            return
        new_node=Node(data)
        # cur_node=Node(data1)
        new_node.next=prev_node.next
        prev_node.next=new_node

ll=Linkedlist()
ll.append(1)
ll.append(2)
ll.append(3)
ll.insertit(ll.head.next,5)
ll.append(4)
ll.prepend(9)

ll.printit()
