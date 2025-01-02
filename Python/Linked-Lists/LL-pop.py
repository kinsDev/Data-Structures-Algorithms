def pop(self):
    # This is an edge case to check whether the length is 0 before popping
    if self.length == 0:
        return None
    temp = self.head
    pre = self.tail
    while(temp.next): # more concise manner of saying while temp is not equal to none
        pre = temp
        temp = temp.next
    # when temp reaches to the last node
    # a node pointing to none, the self.tail will point
    # the previous node which will be where the pre will be located    
    self.tail = pre
    self.tail.next = None
    # Checking whether the length is 0 after popping
    self.length -= 1
    if self.length == 0:
        self.head = None
        self.tail = None