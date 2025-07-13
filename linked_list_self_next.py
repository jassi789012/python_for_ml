class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBeginning(self,data):
        new_node = Node(data)
        if(self.head is None):
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtEnd(self,data):
        new_node = Node(data)
        if self.head is None:
            self.insertAtBeginning(data)
        else:
            itr = self.head
            while itr.next is not None:
                itr = itr.next
            itr.next = new_node

    def insertAtIndex(self,index,data):
        new_node = Node(data)
        if(index<0 or index>self.length()):
            print("Invalid Index")
        elif(index == 0):
            self.insertAtBeginning(data)
        elif(index == self.length):
            self.insertAtEnd(data)
        else:
            itr = self.head
            for i in range(1,index):
                itr = itr.next
            new_node.next = itr.next
            itr.next = new_node

    def delFromBeginning(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            self.head = self.head.next

    def delFromEnd(self):
        if self.head is None:
            print("Linked List is empty")
        elif(self.head.next is None):
            self.delFromBeginning()
        else:
            itr = self.head
            for i in range(1,self.length()-1):
                itr = itr.next
            itr.next = None

    def delAtIndex(self,index):
        if self.head is None:
            print("Linked List is empty")
        elif(index<0 or index>=self.length()):
            print("Invalid Index")
        elif(index == 0):
            self.delFromBeginning()
        elif(index == self.length()):
            self.delFromEnd()
        else:
            itr = self.head
            for i in range(1,index):
                itr = itr.next
            itr.next = itr.next.next
        
    def valueAtIndex(self,index):
        if self.head is None:
            print("Linked List is empty")
        elif(index<0 or index>=self.length()):
            print("Invalid Index")
        else:
            itr = self.head
            for i in range(0,self.length()):
                if(i == index):
                    return itr.data
                itr = itr.next

    def findIndex(self,value):
        if self.head is None:
            print("Linked List is empty")
        else:
            itr = self.head
            for i in range(0,self.length()):
                if(itr.data == value):
                    return i
                itr = itr.next
            print("Value not Found")

    def insertAfterValue(self,after,data):
        index = self.findIndex(after)
        self.insertAtIndex(index+1,data)

    def removeByValue(self,value):
        index = self.findIndex(value)
        self.delAtIndex(index)
        

    def length(self):
        if self.head is None:
            return -1
        else:
            itr = self.head
            count = 0
            while itr is not None:
                itr = itr.next
                count += 1
            return count


    def printInfo(self):
        if(self.head is None):
            print("Linked List is empty")
        else:
            llstr = []
            itr = self.head
            while itr is not None:
                llstr.append(str(itr.data) + "-->")
                itr = itr.next
            return llstr
        

if __name__ == "__main__":
    ll = linkedList()

    ll.insertAtBeginning(40)
    ll.insertAtBeginning(30)
    ll.insertAtBeginning(20)
    ll.insertAtBeginning(10)

    ll.insertAtEnd(50)
    ll.insertAtEnd(60)
    ll.insertAtEnd(70)
    ll.insertAtEnd(80)

    ll.insertAtIndex(1,15)
    ll.insertAtIndex(3,25)
    ll.insertAtIndex(5,35)
    ll.insertAtIndex(7,45)
    ll.insertAtIndex(9,55)
    ll.insertAtIndex(11,65)
    ll.insertAtIndex(13,75)

    ll.delFromBeginning()
    ll.delFromBeginning()
    ll.delFromBeginning()
    ll.delFromBeginning()
    ll.delFromBeginning()
    ll.delFromBeginning()
    ll.delFromBeginning()
    ll.delFromBeginning()

    # ll.delFromEnd()
    # ll.delFromEnd()
    # ll.delFromEnd()
    # ll.delFromEnd()

    ll.delAtIndex(1)
    ll.delAtIndex(0)
    ll.delAtIndex(2)
    ll.delAtIndex(3)

    # print(ll.valueAtIndex(0))
    # print(ll.valueAtIndex(1))
    # print(ll.valueAtIndex(2))

    # print(ll.findIndex(60))
    # print(ll.findIndex(65))
    # print(ll.findIndex(75))
    ll.insertAfterValue(65,70)
    ll.removeByValue(70)
    print("Length of Linked List : "+str(ll.length()))
    print(ll.printInfo())

