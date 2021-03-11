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

    def addFront(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def addEnd(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = newNode

    def addAfter(self, x, data):
        if x is None:
            print("The mentioned node is absent")
            return
        
        newNode = Node(data)
        newNode.next = x
        x.next = newNode

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
    l.addFront(0)
    l.addEnd(1)
    l.addEnd(2)
    l.addEnd(3)
    l.addEnd(4)
    l.traversal()
    l.delete(3)
    l.traversal()