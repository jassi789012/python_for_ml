class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class linkedList:
    
    def __init__(self):
        self.head = None


    def insertAtBegining(self,data):
        node = Node(data, self.head)
        self.head = node

    def insertAtEnd(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def printInfo(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insertAtEnd(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        
        return count

if __name__ == '__main__':
    ll = linkedList()
    # ll.insertAtBegining(5)
    # ll.insertAtBegining(89)
    # ll.insertAtEnd(79)
    ll.insert_values(['banana', 'mango', 'grapes', 'orange'])
    ll.printInfo()
    print(ll.get_length())
