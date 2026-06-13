from tarfile import data_filter


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self,data):
        self.data= data
        self.next = None
    def append(self,data):
        new_Node = Node(data)
        if(self.head is None):
            self.head = Node(data)
            return
    def display(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    print("None")
l1 = LinkedList()
l1.append(10)
l1.append(20)
l1.append(30)
l1.display()
