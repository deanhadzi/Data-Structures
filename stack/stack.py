"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


from singly_linked_list import LinkedList


# class Stack:
#     """
#     LIFO - Last In, First Out
#     Array implementation
#     """

#     def __init__(self):
#         # create an empty array/list
#         self.storage = []

#     def __len__(self):
#         # use python's len function to get the length of the list
#         return len(self.storage)

#     def push(self, value):
#         # use python's append function to add value to the end of the list
#         self.storage.append(value)

#     def pop(self):
#         # check if the stack is empty
#         if len(self.storage) == 0:
#             return None
#         # otherwise pop the last item from the array
#         return self.storage.pop()


class Stack:
    """
    LIFO - Last In, First Out
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

    def push(self, value):
        # add the new value to the end of the LinkedList
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        # check if the stack is already empty
        if self.size == 0:
            return None
        # if not, reduce the size by 1.
        self.size -= 1
        # then remove the last item.
        return self.storage.remove_tail()
