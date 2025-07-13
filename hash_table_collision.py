class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self,key):
        h = 0 
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def __setitem__(self,key,value):
        h = self.get_hash(key)
        found = False
        for idx, e in enumerate(self.arr[h]):
            if len(e) == 2 and e[0] == key:
                self.arr[h][idx] = (key,value)
                found = True
                break
        if not found:
            self.arr[h].append((key,value))

    def __getitem__(self,key):
        h = self.get_hash(key)
        for e in self.arr[h]:
            if e[0] == key:
                return e[1]
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        for index,e in enumerate(self.arr[h]):
            if e[0] == key:
                del self.arr[h][index]

if __name__ == '__main__':
    ht = HashTable()
    ht['march 6'] = 120
    ht['march 6'] = 130
    ht['march 8'] = 67
    ht['march 9'] = 4
    ht['march 17'] = 459


    print(ht['march 6'])
    print(ht['march 17'])

    del ht['march 17']
    print(ht['march 17'])
    
    for i in ht.arr:
        print(i)