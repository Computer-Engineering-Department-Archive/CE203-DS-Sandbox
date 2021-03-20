class Node:
    
    def __init__(self, data): 
        self.data = data 
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:

    def __init__(self):
        self.last = None

    def traversal(self):
        if self.last is None:
            print('None')
            return

        temp = self.last.next

        out = ''
        while True:
            out = str(out) + str(temp.data) + '->'

            if temp == self.last:
                break

            temp = temp.next

        print(out + 'None')

    def add_front(self, data):
        newNode = Node(data)

        if self.last == None:
            self.last = newNode
            newNode.next = newNode
            newNode.prev = newNode
            return

        head = self.last.next
        self.last.next = newNode
        newNode.prev = self.last
        newNode.next = head
        head.prev = newNode

    def add_after(self, x,  data):
        if self.last is None:
            return

        temp = self.last.next

        while temp is not self.last and temp.data != x:
            temp = temp.next
        
        #if we couldn't find the given node in one iteration then it is absent 
        if temp.data != x:
            print("given node is absent.")
            return

        newNode = Node(data)
        newNode.next = temp.next
        newNode.prev = temp
        temp.next.prev = newNode
        temp.next = newNode

        if temp is self.last:
            self.last = newNode

    def add_end(self, data):
        newNode = Node(data)

        if self.last is None:
            self.last = newNode
            newNode.next = self.last
            newNode.prev = self.last
            return

        head = self.last.next

        self.last.next = newNode
        newNode.prev = self.last

        newNode.next = head
        head.prev = newNode
        
        self.last = newNode

    def delete(self, data):
        if self.last is None:
            return

        temp = self.last

        while temp.data != data:
            temp = temp.next

        if temp == self.last:
            if temp.next == temp: #only one node
                self.last = None
            else: #more than one node
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                self.last = temp.prev
        else:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev

        del temp

if __name__ == "__main__":
    l = CircularDoublyLinkedList()

    l.add_end(1)
    l.add_end(2)
    l.add_end(3)

    l.traversal()

    l.delete(1)
    
    l.traversal()