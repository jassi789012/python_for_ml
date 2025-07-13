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
        if(self.head is None):
            self.head = new_node
        else:
            itr = self.head
            while itr.next is not None:
                itr = itr.next
            itr.next = new_node

    def insertAtIndex(self,index,data):
        new_node = Node(data)
        if(index<0 or index>self.length()):
            print("invalid Index")
        elif(index == 0):
            self.insertAtBeginning(data)
        elif(index == self.length()):
            self.insertAtEnd(data)
        else:
            itr = self.head
            for i in range(1,index):
                itr = itr.next
            new_node.next = itr.next
            itr.next = new_node

    def delFromBeginning(self):
        if(self.head is None):
            print("Linked List is empty")
            return
        else:
            self.head = self.head.next
    
    def delFromEnd(self):
        if(self.head is None):
            print("Linked List is empty")
            return
        itr = self.head
        for i in range(0,self.length()-2):
            itr = itr.next
        itr.next = None
        
    def delFromIndex(self,index):
        if(self.head is None):
            print("Linked List is empty")
            return
        elif(index == 0):
            self.delFromBeginning()
        elif(index == self.length()-1):
            self.delFromEnd()
        elif(index<0 or index>=self.length()):
            print("Invalid Index")
        else:
            itr = self.head
            for i in range(index - 1):
                itr = itr.next
            itr.next = itr.next.next
            
            
        

        

    def length(self):
        if(self.head is None):
            return 0
        else:
            itr = self.head
            count = 0
            while itr is not None:
                itr = itr.next
                count += 1
            return count


    def printLL(self):
        if(self.head is None):
            print("Linked List is empty")
            return
        strLL = []
        itr = self.head
        while itr is not None:
            strLL.append(str(itr.data)+"-->")
            itr = itr.next
        return strLL
    

if __name__ == '__main__':
    ll = linkedList()
    ll.insertAtBeginning(10)  #10
    ll.insertAtBeginning(20)  #20-->10
    ll.insertAtBeginning(30)  #30-->20-->10
    ll.insertAtEnd(5)         #30-->20-->10-->5
    ll.insertAtEnd(2.5)       #30-->20-->10-->5-->2.5
    ll.insertAtIndex(1,100)   #30-->100-->20-->10-->5-->2.5
    ll.insertAtIndex(4,400)   #30-->100-->20-->10-->400-->5-->2.5
    ll.delFromBeginning()     #100-->20-->10-->400-->5-->2.5
    ll.delFromEnd()           #100-->20-->10-->400-->5
    ll.delFromIndex(2)

    print(ll.length())
    print(ll.printLL())

