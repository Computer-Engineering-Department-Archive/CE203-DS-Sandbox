class Node():

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList():

    def __init__(self):
        self.head = None

    def traversal(self):
        temp = self.head

        out = ''
        while temp is not None:
            out = str(out) + str(temp.data) + '->'
            temp = temp.next

        print(out + 'None')

    def add_front(self, data):
        # if the list is empty
        if self.head is None:
            self.head = Node(data)
            return

        newNode = Node(data)
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode

    def add_end(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = newNode
        newNode.prev = temp 

    def add_after(self, x, data):
        temp = self.head

        while temp is not None and temp.data != x:
            temp = temp.next

        if temp is None:
            print("given node is absent.")
            return
        
        newNode = Node(data)
        newNode.next = temp.next
        temp.next.prev = newNode
        temp.next = newNode
        newNode.prev = temp

    def delete(self, x):
        if self.head is None:
            return
            
        temp = self.head

        if temp is not None:
            if temp.data == x:
                self.head = temp.next
                del temp
                return

        while temp is not None:
            if temp.data == x:
                break
                
            temp = temp.next

        if temp is None:
            return

        temp.prev.next = temp.next

        if temp.next is not None:
            temp.next.prev = temp.prev
        
        del temp

if __name__ == "__main__":
    l = DoublyLinkedList()

    l.add_front(1)
    l.add_front(2)
    l.add_front(3)
    
    l.traversal()