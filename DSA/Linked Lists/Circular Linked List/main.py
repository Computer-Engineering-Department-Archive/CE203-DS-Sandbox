class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

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

    def add_after(self, x,  data):
        temp = self.head

        while temp is not None and temp.data != x:
            temp = temp.next

        if temp is None:
            print("given node is absent.")
            return

        newNode = Node(data)
        newNode.next = x.next
        x.next = newNode

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
        temp = self.last
        prev = None

        while temp is not None and temp.data != data:
            prev = temp
            temp = temp.next

        if temp is None:
            print("given node is absent.")
            return

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
    l = LinkedList()
    l.add_end(1)
    l.add_end(2)
    l.add_end(3)
    l.add_end(4)
    l.traversal()