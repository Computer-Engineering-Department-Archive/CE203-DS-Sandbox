class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

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
        newNode = Node(data)
        newNode.next = self.head
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

    def add_after(self, x, data):
        temp = self.head

        while temp is not None and temp.data != x:
            temp = temp.next

        if temp is None:
            print("given node is absent.")
            return

        newNode = Node(data)
        newNode.next = temp.next
        temp.next = newNode

    def delete(self, x):
        temp = self.head

        if temp is not None:
            if temp.data == x:
                self.head = temp.next
                del temp
                return
            
        while temp is not None:
            if temp.data == x:
                break
            
            prev = temp
            temp = temp.next

        if temp is None: 
            return
        
        prev.next = temp.next
        del temp

if __name__ == "__main__":
    l = LinkedList()
    l.add_end(1)
    l.add_end(2)
    l.add_end(3)
    l.traversal()