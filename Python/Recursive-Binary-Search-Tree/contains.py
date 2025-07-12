class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def __r_contains(self, current_node, value):
        # this is the simple base case, when we get to a point where current_node is None
        if current_node == None:
            return False

        # if we get to a current_node that matches the value we are looking for, we simply return True - another base case
        if value == current_node.value:
            return True

        # if less than we go left, nut this time by calling our function again(recursion), we go to the left subtree by saying calling current_node.left with our function again
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)

        # same logic for right!
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    # the function below checks whether the value we are lookign for is present in a BST!
    # It works by calling the private helper method __r_contains, passing the root node of the tree (self.root), and the target value.
    # the actual logic is handled recursively by __r_contains
    def r_contains(self, value):
        return self.__r_contains(self.root, value)


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print('BST Contains 27:')
print(my_tree.r_contains(27))

print('\nBST Contains 17:')
print(my_tree.r_contains(17))


"""
    EXPECTED OUTPUT:
    ----------------
    BST Contains 27:
    True

    BST Contains 17:
    False

"""

"""
rBST: Contains
Implement the r_contains method of the BinarySearchTree class. 
This method should recursively search the binary search tree for a given value, 
starting from the root node, and return True if the value is found, and False otherwise.

You should use a private helper method __r_contains to perform the recursive search. 
This method should take two arguments: a current node in the tree, and the value to search for.

The __r_contains method should check whether the current node is None. 
If it is, the method should return False. 
If the value to search for is equal to the value of the current node, the method should return True. 
If the value is less than the value of the current node, the method should call itself recursively 
with the left child node and the value. If the value is greater than the value of the current node, 
the method should call itself recursively with the right child node and the value.

Your implementation of the r_contains method should return the output of the __r_contains method.
"""