class MinHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] < self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    # We will be writing the _sink_down method in the next exercise.
    # But I need to include it here for the tests to work for remove.
    # So, don't peek at this one here.  :-)
    def _sink_down(self, index):
        min_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (left_index < len(self.heap) and
                    self.heap[left_index] < self.heap[min_index]):
                min_index = left_index

            if (right_index < len(self.heap) and
                    self.heap[right_index] < self.heap[min_index]):
                min_index = right_index

            if min_index != index:
                self._swap(index, min_index)
                index = min_index
            else:
                return

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        min_value = self.heap[0]

        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return min_value


myheap = MinHeap()
myheap.insert(12)
myheap.insert(10)
myheap.insert(8)
myheap.insert(6)
myheap.insert(4)
myheap.insert(2)

print(myheap.heap)  # [2, 6, 4, 12, 8, 10]

removed = myheap.remove()
# Removed: 2, Heap: [4, 6, 10, 12, 8]
print(f'Removed: {removed}, Heap: {myheap.heap}')

removed = myheap.remove()
# Removed: 4, Heap: [6, 8, 10, 12]
print(f'Removed: {removed}, Heap: {myheap.heap}')

removed = myheap.remove()
# Removed: 6, Heap: [8, 12, 10]
print(f'Removed: {removed}, Heap: {myheap.heap}')


"""
    EXPECTED OUTPUT:
    ----------------
    [2, 6, 4, 12, 8, 10]
    Removed: 2, Heap: [4, 6, 10, 12, 8]
    Removed: 4, Heap: [6, 8, 10, 12]
    Removed: 6, Heap: [8, 12, 10]

"""


"""
MinHeap: Remove
You have been provided with a MinHeap class that includes the _sink_down method.

** We will be writing the _sink_down method in the next exercise so please do not peek at it in this exercise.  ;-)

The class includes a method for initialization, plus helper methods for getting the left child, the right child, and the parent of a node and swapping elements in the heap.

Your task is to finalize this class by implementing the remove method.

This method is designed to remove the minimum element from the heap, i.e., the root element, and reorganize the heap so it maintains its min heap property. 
The min heap property states that for any given node i other than the root, the value of i is at most the value of its parent.

Here's what your remove method should do in detail:

If the heap is empty, the remove method should return None.

If the heap has only one element, the remove method should remove and return this element.

If the heap has more than one element, the remove method should remove the root of the heap, place the last element in the heap at the root, 
and then call the _sink_down method to reorganize the heap, maintaining the min heap property.



Your remove method should be efficient, aiming for a time complexity of O(log n), where n is the number of elements in the heap.

Remember to consider edge cases where the heap is empty or contains only a few elements.
"""