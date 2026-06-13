from asyncio.windows_events import NULL

class Node:
    def __init_(self,data):
        self.data = data
        self.next = None
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
temp = head
while(temp.next!=NULL):
    temp = temp.next
print(temp.data)
