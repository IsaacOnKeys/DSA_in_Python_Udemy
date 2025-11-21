class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    ### WRITE POP METHOD HERE ###
    def pop(self):
        """this is my pointless 1-pointer solution which is more convoluted than necessary"""
        #in the case of 0 Nodes
        if self.length == 0:
            return None
        # in the case of 1
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        # in the case of 2 or more
        while temp.next != self.tail:
            temp = temp.next
        temp.next = None
        pop_node = self.tail
        self.tail = temp
        self.length -= 1

        return pop_node

        



 


my_linked_list = LinkedList(1)
my_linked_list.append(2)

# (2) Items - Returns 2 Node
print(my_linked_list.pop().value)
# (1) Item -  Returns 1 Node
print(my_linked_list.pop().value)
# (0) Items - Returns None
print(my_linked_list.pop())


"""
    EXPECTED OUTPUT:
    ----------------
    2
    1
    None

"""