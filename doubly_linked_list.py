class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtBeginning(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node

        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node  


    def insertAtEnd(self,data):
        if self.tail is None:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
        
        else:
            new_node = Node(data)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insertAtIndex(self,index,data):
        if(index<0):
            raise Exception("Invalid Index")
        elif(index == 0):
            self.insertAtBeginning(data)
        elif(index == self.length):
            self.insertAtEnd(data)
        else:
            itr = self.head
            for i in range(1,index):
                itr = itr.next
            new_node = Node(data)
            new_node.next = itr.next
            new_node.prev = itr
            itr.next.prev = new_node
            itr.next = new_node

    def delFromBeginning(self):
        if(self.head is None):
            raise Exception("Linked List is empty")
        elif(self.head == self.tail):
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delFromEnd(self):
        if(self.head is None):
            raise Exception("Linked List is empty")
        elif(self.head == self.tail):
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def delFromIndex(self,index):
        if(index<0 or index>=self.length()):
            raise Exception("Invalid Index")
        elif(index == 0):
            self.delFromBeginning()
        elif(index == self.length()-1):
            self.delFromEnd()
        else:
            itr = self.head
            for i in range(1,index):
                itr = itr.next
            itr.next = itr.next.next
            itr.next.prev = itr

    def valueAtIndex(self,index):
        if(index<0 or index>=self.length()):
            raise Exception("Invalid Index")
        elif(index == 0):
            return self.head.data
        elif(index == self.length()-1):
            return self.tail.data
        else:
            itr = self.head
            for i in range(1,index+1):
                itr = itr.next
            return itr.data



    def length(self):
        count = 0
        itr = self.head
        while itr is not None:
            count += 1
            itr = itr.next
        return count

    
    def printInForward(self):
        if self.head is None:
            raise Exception("Linked List is empty")
        
        else:
            itr = self.head
            strll = []
            while itr is not None:
                strll.append(str(itr.data)+"-->")
                itr = itr.next
            return strll
        

    def printInBackword(self):
        if self.head is None:
            raise Exception("Linked List is empty")
        
        else:
            itr = self.tail
            strll = []
            while itr is not None:
                strll.append(str(itr.data)+"-->")
                itr = itr.prev
            return strll
        


if __name__ == "__main__":
    ll = DoublyLL()
    ll.insertAtBeginning(20) 
    ll.insertAtBeginning(10)
    ll.insertAtEnd(30)
    ll.insertAtEnd(40)
    ll.insertAtIndex(2,25)

    # ll.delFromBeginning()
    # ll.delFromBeginning()
    # ll.delFromBeginning()
    # ll.delFromBeginning()

    # ll.delFromEnd()
    # ll.delFromEnd()
    # ll.delFromEnd()
    # ll.delFromEnd()

    # ll.delFromIndex(2)
    # ll.delFromIndex(0)
    # ll.delFromIndex(2)
    # ll.delFromIndex(1)

    # print(ll.valueAtIndex(0))
    # print(ll.valueAtIndex(1))
    # print(ll.valueAtIndex(2))
    # print(ll.valueAtIndex(3))
    # print(ll.valueAtIndex(4))
    print(ll.length())
    print(ll.printInForward()) 
    print(ll.printInBackword())
            