"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
    on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
    on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
        # check if the new node's value is less than the current node value.
            if self.left:
            # if there is already another node on the left, run the insert function
            # recursively on the left node.
                return self.left.insert(value)
            else:
            # otherwise - create a new node and assign it as left child.
                self.left = BSTNode(value)
                return True
        else:
        # do the same on the right node, if the new node value is equal or greater than
        # the current node value.
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BSTNode(value)
                return True

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
        # if the value of the current node matches target - return True
            return True
        else:
            if target < self.value and self.left:
            # if the target is lesser than current node, and there is a left child
            # run the contians method on the left node.
                return self.left.contains(target)
            elif target > self.value and self.right:
            # same logic on the right node.
                return self.right.contains(target)
            else:
            # if there is no child nodes, we reached the leaf node and 
            # didn't find the value. Return False.
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
        # check if there is right node (which by definition will have equal or higher value)
            if self.right.value > self.value:
            # if the value of the right node is higher, call the function again.
                return self.right.get_max()
        else:
        # if we reached the right most leaf node, return its value as this must be the max value.
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        # run a function on the current node.
        if self.left:
        # if there is a left node, run the function on it.
            self.left.for_each(fn)
        if self.right:
        # if there is a right node, run the function on it.
            self.right.for_each(fn)

    # # Part 2 -----------------------

    # # Print all the values in order from low to high
    # # Hint:  Use a recursive, depth first traversal
    # def in_order_print(self):
    #     pass

    # # Print the value of every node, starting with the given node,
    # # in an iterative breadth first traversal
    # def bft_print(self):
    #     pass

    # # Print the value of every node, starting with the given node,
    # # in an iterative depth first traversal
    # def dft_print(self):
    #     pass

    # # Stretch Goals -------------------------
    # # Note: Research may be required

    # # Print Pre-order recursive DFT
    # def pre_order_dft(self):
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self):
    #     pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(21)
print(bst.value)
print(bst.right.value)
print(bst.right.left.value)
print(bst.contains(8))
print(bst.get_max())
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
