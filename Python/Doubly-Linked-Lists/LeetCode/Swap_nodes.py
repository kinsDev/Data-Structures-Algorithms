# Swapping the first and last node.
def swap_first_last(self):
    if self.length < 2:
        return False  # Nothing to swap

    first = self.head
    last = self.tail

    if self.length == 2:
        # Just two nodes: swap head and tail
        self.head, self.tail = self.tail, self.head
        self.head.next = self.tail
        self.head.prev = None
        self.tail.prev = self.head
        self.tail.next = None
        return True

    # Store adjacent nodes
    before_last = last.prev
    after_first = first.next

    # Update head and tail
    self.head = last
    self.tail = first

    # Adjust pointers for new head
    self.head.prev = None
    self.head.next = after_first
    after_first.prev = self.head

    # Adjust pointers for new tail
    self.tail.next = None
    self.tail.prev = before_last
    before_last.next = self.tail
