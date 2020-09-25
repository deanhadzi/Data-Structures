"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

from singly_linked_list import LinkedList


# class Queue:
#     """
#     FIFO - First In, First Out
#     Array implementation
#     """

#     def __init__(self):
#         # create an empty array/list
#         self.storage = []

#     def __len__(self):
#         # use python's len function to get the length of the list
#         return len(self.storage)

#     def enqueue(self, value):
#         # use python's insert function to add value to the start of the list
#         self.storage.insert(0, value)

#     def dequeue(self):
#         # check if the queue is empty
#         if len(self.storage) == 0:
#             return None
#         # otherwise pop the last item from the array
#         return self.storage.pop()


class Queue:
    """
    FIFO - First In, First Out
    LinkedList implementation
    """

    def __init__(self):
        # create a counter that keeps track of the list length.
        self.size = 0
        # instantiate the storage container with LinkedList class.
        self.storage = LinkedList()

    def __len__(self):
        # return the counter value.
        return self.size

    def enqueue(self, value):
        # use python's insert function to add value to the start of the list
        self.storage.add_to_head(value)
        self.size += 1

    def dequeue(self):
        # check if the queue is empty
        if self.size == 0:
            return None
        # if not, reduce the size by 1.
        self.size -= 1
        # then remove the last item.
        return self.storage.remove_tail()
