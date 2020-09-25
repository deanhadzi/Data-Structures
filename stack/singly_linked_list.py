# Creating the Node Class


class Node:
    def __init__(self, value, next_node=None):
        # value that the node is holding
        self.value = value
        # ref to the next node in the chain
        self.next_node = next_node

    def get_value(self):
        """
        Method to get the value of node.
        """
        return self.value

    def get_next(self):
        """
        Method to get the node's 'next_node'
        """
        return self.next_node

    def set_next_node(self, new_next):
        """
        Method to update the node's 'next_node' to the new_next.
        """
        self.next_node = new_next


# Let's make LinkedList Class.


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        # wrap the value in a new Node
        new_node = Node(value)
        # check if the linked list is empty
        if self.head == None and self.tail == None:
            # set the head and tail to the new node
            self.head = new_node
            self.tail = new_node
        # otherwise the list must have at least one item in it
        else:
            # update the last node's "next_node" to the new node
            self.tail.set_next_node(new_node)
            # update the self.tail to point to the new node
            self.tail = new_node

    def remove_tail(self):
        """
        Remove the last node in the chain and return its value.
        """
        # check for empty list
        if self.head == None and self.tail == None:
            return None
        # check if there is only one node
        if self.head == self.tail:
            # store the value of the node that we are going to remove
            value = self.tail.get_value()
            # remove the node
            self.head = None
            self.tail = None
            return value
        # otherwise
        else:
            # store the value of the node that we are going to remove
            value = self.tail.get_value()
            # we need to set the self.tail to the second to last node
            # start from the head
            current_node = self.head

            # loop through the list until you reach next to last node.
            while current_node.get_next() != self.tail:
                current_node = current_node.get_next()

            # assign the next to last node as the tail node.
            self.tail = current_node
            # set the pointer of the new last node to None.
            self.tail.set_next_node(None)
            # return the value of the removed node.
            return value

    def add_to_head(self, value):
        # wrap the value in a new Node
        new_node = Node(value)
        # check if the linked list is empty
        if self.head == None and self.tail == None:
            # set the head and tail to the new node
            self.head = new_node
            self.tail = new_node
        # otherwise the list must have at least one item in it
        else:
            # make new node point to the old head
            new_node.set_next_node(self.head)
            # reassign the new node to be the head node.
            self.head = new_node

    def remove_head(self):
        """
        Remove the first node in the chain and return its value.
        """
        # check for empty list
        if self.head == None and self.tail == None:
            return None
        # check if there is only one node
        if self.head == self.tail:
            # store the value of the node that we are going to remove
            value = self.head.get_value()
            # remove the node
            self.head = None
            self.tail = None
            return value
        # otherwise
        else:
            # store the value of the node that we are going to remove
            value = self.head.get_value()
            self.head = self.head.get_next()
            return value
