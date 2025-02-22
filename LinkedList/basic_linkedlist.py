class Node:
    def __init__(self, data):
        self.data =  data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # add a new node 
    # insert at specific location
    # remove the last node at specific location
    # traverse the linked list

    def addNode(self, data):
        if self.head == None:
            self.head = Node(data)
            return

        currentnode = self.head 
        while currentnode.next:
            currentnode =  currentnode.next

        currentnode.next = Node(data)



    def addnode_specific(self, data, location):
        if self.head == None:
            self.head = Node(data)
            return

        if location == 0:  # Insert at head
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
            return


        currentnode = self.head
        counter = 0
        while currentnode and counter+1 != location:
            counter += 1
            currentnode = currentnode.next


        if currentnode is not None:
            newnode = Node(data)
            newnode.next = currentnode.next
            currentnode.next = newnode
        
        else:
            print("index not there")

    def traverse(self):
        currentnode = self.head
        if self.head ==  None:
            return
        counter = 0
        while currentnode:
            print(counter, currentnode.data)
            counter =  counter + 1
            currentnode = currentnode.next


    def deletenode_specific(self, location):

        counter = 0

        currentnode = self.head

        while currentnode.next:
            if counter +1 != location:
                currentnode = currentnode.next

            else:
                currentnode.next = currentnode.next.next

            counter = counter + 1
        return




ll = LinkedList()
ll.addNode('a')
ll.addNode('b')
ll.addNode('c')
ll.addNode('d')
ll.addnode_specific('e', 3)
ll.deletenode_specific(2)
print('traverse')
ll.traverse()

