#adatszerkezetek
#1. Lista
class Node: #lista elem létrehozása
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    head=None
    def appendFront(self,data):
        new_e=Node(data)
        new_e.next=self.head
        self.head=new_e

    def appendBack(self,data):
        new_e=Node(data)
        if self.head==None:
            self.head=new_e
        else:
            current_item=self.head
            while current_item.next!=None:
                current_item=current_item.next
            current_item.next=new_e

    def remove(self,element):
        tmp=self.head
        previous=None
        while tmp!=None:
            if tmp.data==element:
                if previous==None:
                    self.head=self.head.next
                else:
                    previous.next=tmp.next
            previous=tmp
            tmp=tmp.next

    def show(self):
        tmp=self.head
        print("A lista elemei")
        while tmp!=None:
            print(tmp.data,"->",end="")
            tmp=tmp.next
        print("None")

    def beszur_kozepre(self,ezutan,ezt):
        tmp=self.head
        ezt=Node(ezt)
        while tmp!=None:
            if tmp.data==ezutan:
                ezt.next=tmp.next
                tmp.next=ezt
            tmp=tmp.next


s=LinkedList()
s.appendFront(23)
s.appendFront(42)
s.appendBack(11)
s.appendBack(77)
#s.show()
#s.remove(77)
s.show()
s.beszur_kozepre(23,24)
s.show()
s.beszur_kozepre(77,24)
s.show()