class LinkedListNode:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class CircularLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.curr_node = None
        self.length = 0

    def append(self, value):
        """
        Add new item at the end of the circular linked list.
        """
        if self.head is None:
            self.head = LinkedListNode(value)
            self.tail = self.head
            self.tail.next = self.head
        else:
            node = LinkedListNode(value)
            self.tail.next = node
            node.next = self.head
            self.tail = node
        self.length += 1

    def next(self) -> LinkedListNode:
        """
        Get the next node of the circular linked list.
        """
        if self.head is None:
            raise IndexError()

        if self.curr_node is None:
            self.curr_node = self.head
            return self.curr_node

        self.curr_node = self.curr_node.next
        return self.curr_node

    def __len__(self) -> int:
        return self.length
