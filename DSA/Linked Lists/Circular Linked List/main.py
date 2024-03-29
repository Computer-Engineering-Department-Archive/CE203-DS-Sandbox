class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:

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

    def add_first(self, data):
        newNode = Node(data)

        if self.last is None:
            self.last = newNode
            newNode.next = newNode
            return

        head = self.last.next
        self.last.next = newNode
        newNode.next = head

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
        temp.next = newNode

        if temp is self.last:
            self.last = newNode

    def add_end(self, data):
        newNode = Node(data)

        if self.last is None:
            self.last = newNode
            newNode.next = newNode
            return

        newNode.next = self.last.next
        self.last.next = newNode
        self.last = newNode

    def delete(self, data):
        if self.last is None:
            return

        temp = self.last
        prev = temp

        #get the second last element
        while prev.next != self.last:
            prev = prev.next

        while temp.data != data:
            prev = temp
            temp = temp.next

        if temp == self.last:
            if temp.next == temp: #only one node
                self.last = None
            else: #more than one node
                prev.next = temp.next
                self.last = prev
        else:
            prev.next = temp.next

        del temp

if __name__ == "__main__":
    l = CircularLinkedList()

    l.add_first(1)
    l.add_first(2)
    l.add_first(3)
    
    l.traversal()

    l.delete(3)

    l.traversal()