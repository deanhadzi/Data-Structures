"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        # create a new node and increment the length
        new_node = ListNode(value)
        self.length += 1
        # check if the list is empty
        if self.head == None and self.tail == None:
            # if it's empty, set head and tail node to be the new node.
            self.head = new_node
            self.tail = new_node
        else:
            # adjust the new node ref to the old head node.
            new_node.next = self.head
            # adjust the old head node ref to the new head node.
            self.head.prev = new_node
            # reassign the head node.
            self.head = new_node

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        # save the value
        value = self.head.value
        # use delete method to remove the head
        self.delete(self.head)
        return value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        # create a new node and increment the length
        new_node = ListNode(value)
        self.length += 1
        # check if the list is empty
        if self.head == None and self.tail == None:
            # if it's empty, set head and tail node to be the new node.
            self.head = new_node
            self.tail = new_node
        else:
            # adjust the new node ref to the old tail node.
            new_node.prev = self.tail
            # adjust the old tail node ref to the new tail node.
            self.tail.next = new_node
            # reassign the tail node.
            self.tail = new_node

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        # save the value
        value = self.tail.value
        # use delete method to remove the tail
        self.delete(self.tail)
        return value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        # if the node is already at the head, do nothing.
        if node == self.head:
            return None
        # otherwise save the value
        value = node.value
        # if the node is tail, use already existing method
        if node == self.tail:
            self.remove_from_tail()
        # if the node is in the middle, rearrange the references.
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.length -= 1
        # use existing method to add to the head.
        self.add_to_head(value)

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        # if the node is already at the tail, do nothing.
        if node == self.tail:
            return None
        # otherwise save the value
        value = node.value
        # if the node is head, use already existing method
        if node == self.head:
            self.remove_from_head()
        # if the node is in the middle, rearrange the references.
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.length -= 1
        # use existing method to add to the head.
        self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        # Case 1: list is empty
        if self.head == None and self.tail == None:
            return None
        # Case 2: list only has one item
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # Case 3: removing the head node
        elif self.head == node:
            self.head = node.next
            self.head.prev = None
        # Case 4: removing the tail node
        elif self.tail == node:
            self.tail = node.prev
            self.tail.next = None
        # Cast 5: removing the middle node
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        # reduce length by 1.
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        # assign head value as max value
        max_val = self.head.value
        # create a starting point of a loop
        current = self.head
        # iterate through the loop until the max value is reached.
        while current:
            if current.value > max_val:
                max_val = current.value
            current = current.next
        return max_val
