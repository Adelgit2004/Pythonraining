class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    def display(self):
        count_o = 0
        count_e = 0
        temp = self.head
        while temp:
            if(temp.data%2!=0):
                count_o+=1
            else:
                count_e+=1
            temp = temp.next
        print(count_o,count_e)

l1 = LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.display()




